#!/usr/bin/env python3
"""Retarget Vicinae's Qt 6 QML private-ABI requirement to Fedora 44's ABI."""
import struct, sys
p = sys.argv[1]
b = bytearray(open(p, 'rb').read())
shoff = struct.unpack_from('<Q', b, 0x28)[0]; ents = struct.unpack_from('<H', b, 0x3a)[0]
num = struct.unpack_from('<H', b, 0x3c)[0]; si = struct.unpack_from('<H', b, 0x3e)[0]
ss = [struct.unpack_from('<IIQQQQIIQQ', b, shoff+i*ents) for i in range(num)]
sn = ss[si]; names = b[sn[4]:sn[4]+sn[5]]
def sec(n):
    for s in ss:
        q=s[0]; z=names.find(b'\0',q)
        if names[q:z] == n.encode(): return s
    raise SystemExit('missing '+n)
ds=sec('.dynstr'); vr=sec('.gnu.version_r'); base=ds[4]
def string(off):
    z=b.find(b'\0',base+off); return bytes(b[base+off:z])
new = None
o = base
while o < base + ds[5]:
    z = b.find(b'\0', o, base + ds[5])
    if b[o:z] == b'Qt_6': new = o - base
    o = z + 1
if new is None: raise SystemExit('Qt_6 string missing')
def elf_hash(s):
    h = g = 0
    for c in s:
        h = (h << 4) + c; g = h & 0xf0000000
        if g: h ^= g >> 24
        h &= ~g
    return h
o=vr[4]
while o < vr[4]+vr[5]:
    _,cnt,fileoff,aux,nxt=struct.unpack_from('<HHIII',b,o)
    if string(fileoff) == b'libQt6Qml.so.6':
        a=o+aux
        for _ in range(cnt):
            noff=struct.unpack_from('<I',b,a+8)[0]
            if string(noff) == b'Qt_6_PRIVATE_API':
                struct.pack_into('<I', b, a, elf_hash(b'Qt_6'))
                struct.pack_into('<I',b,a+8,new); open(p,'wb').write(b); sys.exit(0)
            a += struct.unpack_from('<I',b,a+12)[0]
    if not nxt: break
    o += nxt
raise SystemExit('Vicinae QML ABI requirement missing')
