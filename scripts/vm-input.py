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

    if args.action == "key":
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
            events += [{"type": "btn", "data": {"button": "left", "down": True}},
                       {"type": "btn", "data": {"button": "left", "down": False}}]
    elif args.action == "button":
        events = [{"type": "btn", "data": {"button": args.name, "down": True}},
                  {"type": "btn", "data": {"button": args.name, "down": False}}]
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
            response = qmp(sock, {"execute": "input-send-event", "arguments": {"events": events}})
            if "error" in response:
                raise RuntimeError(response["error"])
    except (OSError, TimeoutError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"VM input failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
