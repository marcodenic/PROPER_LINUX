# Fedora build containers

All Proper builders use Fedora's official x86-64 Fedora 44 container:

- Registry: `quay.io/fedora/fedora`
- Discovery tag: `44` (used only when reviewing a pin update)
- Linux/amd64 manifest: `sha256:aadc45e503a9a4df93b2a30102151d5286d2869c6ba44b8fbf3918abd9ca3862`
- Parent index observed on 2026-09-06: `sha256:3d020c33fbb50af70acaf673e0e6cad94ccef310e9fce6856112e077a5402117`
- Provenance: [Fedora's container distribution](https://fedoraproject.org/misc/).
  Fedora RPMs retain their individual licences.

This manifest was downloaded into empty Podman storage and its `/etc/os-release`
verified as Fedora Linux 44. Builds use the manifest digest, never the moving tag.
Container package installation still uses Fedora repositories; a pinned base
image does not freeze every build dependency or imply bit-identical output.

## Updating the pin

Inspect the official `44` tag and select its Linux/amd64 manifest. Pull the
selected digest into an empty temporary Podman store, run it and verify its
Fedora release and architecture. Update the four Containerfiles in this
directory (including `firmware/Containerfile`), both references in
`../scripts/build-rpms`, the firmware lock's `EDK2_BUILDER_BASE_DIGEST`, and this
record together. Retain an exact digest; do not silently fall back to a tag.

Then build from a fresh checkout and empty output and container caches. Preserve
the revision, patch if any, environment report, build log and ISO checksum.
Validate installation before advertising an installation-tested image.

Registry retention is external to Proper. A digest proves content identity,
not continued availability. The previous two pins returned `MANIFEST_UNKNOWN`
on 2026-09-06; an existing developer cache can conceal that failure. Repeat the
uncached input check before a release, and re-pin and rebuild if an input has
been removed.
