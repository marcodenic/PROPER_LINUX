#!/usr/bin/python3
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

import importlib.util
from importlib.machinery import SourceFileLoader
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest import mock


HELPER = Path(__file__).parents[1] / "proper-agent-status"
FAKE_CODEX = Path(__file__).with_name("fake_codex")
STATUS_SHADE = Path(__file__).parents[1] / "status-shade/contents/ui/main.qml"
STATUS_SHADE_FULL = Path(__file__).parents[1] / "status-shade/contents/ui/FullRepresentation.qml"
SPEC = importlib.util.spec_from_loader("proper_agent_status", SourceFileLoader("proper_agent_status", str(HELPER)))
assert SPEC and SPEC.loader
agent_status = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(agent_status)


class AgentStatusTest(unittest.TestCase):
    def test_status_shade_is_a_normal_shelf_applet(self) -> None:
        qml = STATUS_SHADE.read_text()
        self.assertNotIn("Plasmoid.constraintHints", qml)
        self.assertIn('Plasmoid.title: "Command Centre"', qml)

    def test_status_shade_uses_one_bounded_shell_surface(self) -> None:
        qml = STATUS_SHADE_FULL.read_text()
        self.assertIn(
            "implicitWidth: Math.min(720, Math.max(640, Screen.width - 96))",
            qml,
        )
        self.assertNotIn("FrameSvgItem", qml)
        self.assertNotIn("widgets/panel-background", qml)
        self.assertIn('text: "Command Centre"', qml)
        self.assertNotIn("B A N D W I D T H", qml)
        self.assertNotIn("60 seconds ago", qml)
        self.assertNotIn("closeArea", qml)
        self.assertNotIn("not installed", qml.lower())

    def test_codex_adapter_speaks_the_supported_app_server_protocol(self) -> None:
        result = agent_status.read_codex_rate_limits(str(FAKE_CODEX), timeout=2)
        limits = result["rateLimitsByLimitId"]["codex"]
        self.assertEqual(limits["primary"]["usedPercent"], 38)
        self.assertEqual(limits["secondary"]["windowDurationMins"], 10_080)

    def test_codex_windows_normalize_primary_and_secondary(self) -> None:
        windows, plan = agent_status._codex_windows(
            {
                "rateLimits": {
                    "planType": "pro",
                    "primary": {"usedPercent": 31.25, "windowDurationMins": 300, "resetsAt": 2_000_000_000},
                    "secondary": {"usedPercent": 8, "windowDurationMins": 10_080, "resetsAt": 2_000_100_000},
                }
            }
        )
        self.assertEqual(plan, "pro")
        self.assertEqual([window["label"] for window in windows], ["5-hour", "7-day"])
        self.assertEqual(windows[0]["remaining_percent"], 68.8)
        self.assertEqual(windows[1]["remaining_percent"], 92.0)

    def test_codex_prefers_named_limit(self) -> None:
        windows, _ = agent_status._codex_windows(
            {
                "rateLimits": {"primary": {"usedPercent": 99, "windowDurationMins": 300, "resetsAt": 2_000_000_000}},
                "rateLimitsByLimitId": {
                    "codex": {"primary": {"usedPercent": 12, "windowDurationMins": 300, "resetsAt": 2_000_000_000}}
                },
            }
        )
        self.assertEqual(windows[0]["used_percent"], 12.0)

    def test_claude_cache_contains_only_rate_limits(self) -> None:
        payload = {
            "session_id": "private-session",
            "workspace": {"current_dir": "/private/project"},
            "rate_limits": {
                "five_hour": {"used_percentage": 42, "resets_at": "2033-05-18T03:33:20Z"},
                "seven_day": {"used_percentage": 15.5, "resets_at": 2_000_100_000},
            },
        }
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            stdin = mock.Mock()
            stdin.buffer = io.BytesIO(json.dumps(payload).encode())
            stdout = mock.Mock()
            stdout.buffer = io.BytesIO()
            with mock.patch.dict(os.environ, {"HOME": str(home), "XDG_CACHE_HOME": str(home / "cache"), "XDG_CONFIG_HOME": str(home / "config")}, clear=False), mock.patch.object(Path, "home", return_value=home), mock.patch.object(sys, "stdin", stdin), mock.patch.object(sys, "stdout", stdout):
                self.assertEqual(agent_status.capture_claude(), 0)
                cached = json.loads((home / "cache/proper-linux/agent-status/claude.json").read_text())
        self.assertNotIn("session_id", cached)
        self.assertNotIn("workspace", cached)
        self.assertEqual(cached["rate_limits"]["five_hour"]["used_percentage"], 42.0)

    def test_claude_hook_preserves_and_restores_existing_status_line(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            settings_path = home / ".claude/settings.json"
            settings_path.parent.mkdir(parents=True)
            original_status_line = {"type": "command", "command": "/usr/local/bin/my-status", "padding": 1}
            settings_path.write_text(json.dumps({"theme": "dark", "statusLine": original_status_line}))
            environment = {"HOME": str(home), "XDG_CONFIG_HOME": str(home / "config")}
            with mock.patch.dict(os.environ, environment, clear=False), mock.patch.object(Path, "home", return_value=home), mock.patch("builtins.print"):
                self.assertEqual(agent_status.install_claude_hook(), 0)
                installed = json.loads(settings_path.read_text())
                self.assertEqual(installed["statusLine"]["command"], agent_status.CLAUDE_CAPTURE_COMMAND)
                self.assertEqual(installed["statusLine"]["padding"], 1)
                self.assertTrue(agent_status._claude_hook_is_installed())
                self.assertEqual(agent_status.remove_claude_hook(), 0)
                restored = json.loads(settings_path.read_text())
                self.assertFalse(agent_status._claude_hook_is_installed())
            self.assertEqual(restored["statusLine"], original_status_line)
            self.assertEqual(restored["theme"], "dark")

    def test_expired_cached_windows_are_not_displayed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            binary = home / ".local/bin/claude"
            binary.parent.mkdir(parents=True)
            binary.write_text("#!/bin/sh\n")
            binary.chmod(0o755)
            cache = home / "cache/proper-linux/agent-status/claude.json"
            cache.parent.mkdir(parents=True)
            cache.write_text(json.dumps({"rate_limits": {"five_hour": {"used_percentage": 10, "resets_at": 100}}}))
            environment = {
                "HOME": str(home),
                "PATH": "/usr/bin:/bin",
                "XDG_CACHE_HOME": str(home / "cache"),
            }
            with mock.patch.dict(os.environ, environment, clear=False), mock.patch.object(Path, "home", return_value=home):
                provider = agent_status.claude_provider(now=200)
            self.assertEqual(provider["status"], "waiting")
            self.assertEqual(provider["windows"], [])

    def test_agent_panel_is_seeded_once_only_after_an_agent_is_installed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            environment = {"HOME": str(home), "XDG_CONFIG_HOME": str(home / "config")}
            with mock.patch.dict(os.environ, environment, clear=False), mock.patch.object(Path, "home", return_value=home), mock.patch.object(agent_status, "_find_agent_binary", side_effect=lambda name: "/usr/bin/codex" if name == "codex" else None), mock.patch.object(agent_status, "_run_plasma_script", return_value=True) as run:
                self.assertEqual(agent_status.ensure_agent_panel(), 0)
                self.assertEqual(agent_status.ensure_agent_panel(), 0)
            self.assertEqual(run.call_count, 1)
            script = run.call_args.args[0]
            self.assertIn('new Panel("org.kde.panel")', script)
            self.assertIn('panel.alignment = "right"', script)
            self.assertIn("panel.height = 56", script)
            self.assertIn("panel.minimumLength = 132", script)
            self.assertIn("panel.floating = true", script)
            self.assertIn('panel.opacity = "translucent"', script)

    def test_global_shade_is_seeded_once_without_an_agent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            environment = {"HOME": str(home), "XDG_CONFIG_HOME": str(home / "config")}
            with mock.patch.dict(os.environ, environment, clear=False), mock.patch.object(Path, "home", return_value=home), mock.patch.object(agent_status, "_run_plasma_script", return_value=True) as run:
                self.assertEqual(agent_status.ensure_shade(), 0)
                self.assertEqual(agent_status.ensure_shade(), 0)
            self.assertEqual(run.call_count, 1)
            script = run.call_args.args[0]
            self.assertIn('panel.widgets("org.kde.plasma.icontasks")', script)
            self.assertIn('panel.widgets("org.kde.plasma.systemtray")', script)
            self.assertIn('panel.widgets("org.kde.plasma.digitalclock")', script)
            self.assertIn('if (!found && shelf === null)', script)
            self.assertIn('print("proper-desktop-layout-pending")', script)
            self.assertNotIn('new Panel("org.kde.panel")', script)
            self.assertIn('shelf.addWidget("com.properlinux.statusshade")', script)
            self.assertIn('shade.globalShortcut = "Meta+S"', script)

    def test_system_snapshot_reduces_live_counters(self) -> None:
        with mock.patch.object(agent_status, "_read_cpu_times", side_effect=[(100, 30), (200, 50)]), mock.patch.object(agent_status, "_default_network_interface", return_value="eth0"), mock.patch.object(agent_status, "_network_counters", side_effect=[(1000, 2000), (3000, 2400)]), mock.patch.object(agent_status, "_network_name", return_value="Studio LAN"), mock.patch.object(agent_status, "_memory_usage", return_value=(4_000, 10_000)), mock.patch.object(agent_status, "_storage_usage", return_value=(20_000, 100_000)), mock.patch.object(agent_status, "_temperature_celsius", return_value=54.2), mock.patch.object(agent_status.time, "sleep"), mock.patch.object(agent_status.time, "monotonic", side_effect=[10.0, 10.2]):
            result = agent_status.system_snapshot(sample_seconds=0.2)
        self.assertEqual(result["system"]["cpu_percent"], 80.0)
        self.assertEqual(result["system"]["temperature_c"], 54.2)
        self.assertEqual(result["system"]["memory_used_bytes"], 4_000)
        self.assertEqual(result["network"]["name"], "Studio LAN")
        self.assertEqual(result["network"]["download_bytes_per_second"], 10_000)
        self.assertEqual(result["network"]["upload_bytes_per_second"], 2_000)


if __name__ == "__main__":
    unittest.main()
