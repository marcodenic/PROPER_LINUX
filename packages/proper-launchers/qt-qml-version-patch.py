#!/usr/bin/env python3
"""Give Fedora's Qt 6.11 QML private ABI the name used by Vicinae 0.24."""
import struct
import sys

path = sys.argv[1]
b = bytearray(open(path, "rb").read())
shoff = struct.unpack_from("<Q", b, 0x28)[0]
shents = struct.unpack_from("<H", b, 0x3A)[0]
shnum = struct.unpack_from("<H", b, 0x3C)[0]
shstr = struct.unpack_from("<H", b, 0x3E)[0]
sections = [struct.unpack_from("<IIQQQQIIQQ", b, shoff + i * shents) for i in range(shnum)]
names = b[sections[shstr][4]:sections[shstr][4] + sections[shstr][5]]
def section(name):
    for s in sections:
        start = s[0]
        if names[start:names.find(b"\0", start)] == name.encode():
            return s
    raise SystemExit("missing section " + name)

dynstr = section(".dynstr")
dynsym = section(".dynsym")
verdef = section(".gnu.version_d")
base, size = dynstr[4], dynstr[5]

# Collect string offsets used by the dynamic symbol/version tables.
used = {0}
for off in range(dynsym[4], dynsym[4] + dynsym[5], dynsym[9] or 24):
    used.add(struct.unpack_from("<I", b, off)[0])
o = verdef[4]
target_name_offset = None
while o < verdef[4] + verdef[5]:
    _, _, index, _, _, aux, nxt = struct.unpack_from("<HHHHIII", b, o)
    ao = o + aux
    name_offset, _ = struct.unpack_from("<II", b, ao)
    used.add(name_offset)
    if index == 3:
        target_name_offset = ao
    if not nxt:
        break
    o += nxt
if target_name_offset is None:
    raise SystemExit("Qt private version definition not found")

# Reuse an unreferenced string slot; this keeps ELF offsets and segment sizes stable.
candidate = None
end = base + size
o = base
while o < end:
    z = b.find(b"\0", o, end)
    if z < 0:
        break
    if o not in used and z - o >= len(b"Qt_6_PRIVATE_API"):
        candidate = o
        break
    o = z + 1
if candidate is None:
    raise SystemExit("no unused dynamic-string slot available")
b[candidate:candidate + len(b"Qt_6_PRIVATE_API")] = b"Qt_6_PRIVATE_API"
struct.pack_into("<I", b, target_name_offset, candidate - base)
open(path, "wb").write(b)
