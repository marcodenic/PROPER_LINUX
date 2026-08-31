#!/usr/bin/env python3
"""Send one verified QMP input event to a disposable Proper Linux VM.

Coordinates are framebuffer pixels and are scaled to QEMU's absolute tablet
range.  The helper negotiates QMP capabilities and bounds every socket read so
an unresponsive VM cannot leave an overnight harness wedged.
"""
import argparse
import json
import socket
import sys
import time


def qmp(sock: socket.socket, request: dict) -> dict:
    sock.sendall((json.dumps(request) + "\n").encode())
    data = b""
    while b"\n" not in data:
        data += sock.recv(65536)
    return json.loads(data.split(b"\n", 1)[0])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("qmp_socket")
    sub = parser.add_subparsers(dest="action", required=True)
    key = sub.add_parser("key")
    key.add_argument("qcode")
    key_down = sub.add_parser("key-down")
    key_down.add_argument("qcode")
    key_up = sub.add_parser("key-up")
    key_up.add_argument("qcode")
    combo = sub.add_parser("combo")
    combo.add_argument("qcodes", nargs="+", help="keys held in order, then released in reverse order")
    type_text = sub.add_parser("type")
    type_text.add_argument("text", help="ASCII text to type into the focused guest control")
    click = sub.add_parser("click")
    click.add_argument("x", type=int)
    click.add_argument("y", type=int)
    click.add_argument("--width", type=int, default=1920)
    click.add_argument("--height", type=int, default=1080)
    move = sub.add_parser("move")
    move.add_argument("x", type=int)
    move.add_argument("y", type=int)
    move.add_argument("--width", type=int, default=1920)
    move.add_argument("--height", type=int, default=1080)
    button = sub.add_parser("button")
    button.add_argument("name", choices=("left", "right", "middle"), default="left")
    button_down = sub.add_parser("button-down")
    button_down.add_argument("name", choices=("left", "right", "middle"), default="left")
    button_up = sub.add_parser("button-up")
    button_up.add_argument("name", choices=("left", "right", "middle"), default="left")
    args = parser.parse_args()

    followup_events = None
    event_frames = None
    if args.action == "type":
        unshifted = {
            " ": "spc", "-": "minus", "=": "equal", "[": "bracket_left",
            "]": "bracket_right", "\\": "backslash", ";": "semicolon",
            "'": "apostrophe", "`": "grave_accent", ",": "comma", ".": "dot",
            "/": "slash",
        }
        shifted = {
            "!": "1", "@": "2", "#": "3", "$": "4", "%": "5", "^": "6",
            "&": "7", "*": "8", "(": "9", ")": "0", "_": "minus", "+": "equal",
            "{": "bracket_left", "}": "bracket_right", "|": "backslash",
            ":": "semicolon", '"': "apostrophe", "~": "grave_accent", "<": "comma",
            ">": "dot", "?": "slash",
        }
        # Send every transition as its own QMP frame. Long event arrays can be
        # truncated by the input path, and collapsed transitions lose keys.
        event_frames = []
        for character in args.text:
            needs_shift = character.isalpha() and character.isupper()
            if character.isalpha():
                qcode = character.lower()
            elif character.isdigit():
                qcode = character
            elif character in unshifted:
                qcode = unshifted[character]
            elif character in shifted:
                qcode = shifted[character]
                needs_shift = True
            else:
                parser.error(f"unsupported character for QMP typing: {character!r}")
            if needs_shift:
                event_frames.append([{"type": "key", "data": {"down": True, "key": {"type": "qcode", "data": "shift"}}}])
            event_frames.extend([
                [{"type": "key", "data": {"down": True, "key": {"type": "qcode", "data": qcode}}}],
                [{"type": "key", "data": {"down": False, "key": {"type": "qcode", "data": qcode}}}],
            ])
            if needs_shift:
                event_frames.append([{"type": "key", "data": {"down": False, "key": {"type": "qcode", "data": "shift"}}}])
    elif args.action == "key":
        events = [
            {"type": "key", "data": {"down": True, "key": {"type": "qcode", "data": args.qcode}}},
            {"type": "key", "data": {"down": False, "key": {"type": "qcode", "data": args.qcode}}},
        ]
    elif args.action in ("key-down", "key-up"):
        events = [{"type": "key", "data": {
            "down": args.action == "key-down",
            "key": {"type": "qcode", "data": args.qcode},
        }}]
    elif args.action == "combo":
        events = [
            {"type": "key", "data": {"down": True, "key": {"type": "qcode", "data": qcode}}}
            for qcode in args.qcodes
        ]
        events += [
            {"type": "key", "data": {"down": False, "key": {"type": "qcode", "data": qcode}}}
            for qcode in reversed(args.qcodes)
        ]
    elif args.action in ("click", "move"):
        if not (0 <= args.x < args.width and 0 <= args.y < args.height):
            parser.error("click coordinates must be inside the framebuffer")
        events = [{"type": "abs", "data": {"axis": "x", "value": round(args.x * 32767 / (args.width - 1))}},
                  {"type": "abs", "data": {"axis": "y", "value": round(args.y * 32767 / (args.height - 1))}}]
        if args.action == "click":
            # Keep press and release in separate QMP input frames. Sending both
            # in one frame moves the absolute pointer but libinput can collapse
            # the zero-duration button transition and never deliver a click.
            events.append({"type": "btn", "data": {"button": "left", "down": True}})
            followup_events = [{"type": "btn", "data": {"button": "left", "down": False}}]
    elif args.action == "button":
        events = [{"type": "btn", "data": {"button": args.name, "down": True}}]
        followup_events = [{"type": "btn", "data": {"button": args.name, "down": False}}]
    elif args.action in ("button-down", "button-up"):
        events = [{"type": "btn", "data": {
            "button": args.name,
            "down": args.action == "button-down",
        }}]

    try:
        with socket.socket(socket.AF_UNIX) as sock:
            sock.settimeout(3)
            sock.connect(args.qmp_socket)
            greeting = b""
            while b"\n" not in greeting:
                greeting += sock.recv(65536)
            response = qmp(sock, {"execute": "qmp_capabilities"})
            if "error" in response:
                raise RuntimeError(response["error"])
            if event_frames is not None:
                for frame in event_frames:
                    response = qmp(sock, {"execute": "input-send-event", "arguments": {"events": frame}})
                    if "error" in response:
                        raise RuntimeError(response["error"])
                    time.sleep(0.006)
            else:
                response = qmp(sock, {"execute": "input-send-event", "arguments": {"events": events}})
                if "error" in response:
                    raise RuntimeError(response["error"])
            if followup_events:
                time.sleep(0.08)
                response = qmp(sock, {
                    "execute": "input-send-event",
                    "arguments": {"events": followup_events},
                })
                if "error" in response:
                    raise RuntimeError(response["error"])
    except (OSError, TimeoutError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"VM input failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
