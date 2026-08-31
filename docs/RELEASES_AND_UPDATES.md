# Proper Linux releases and updates

## The short answer

Proper Linux does not need a new ISO for every change. The ISO installs a
tested snapshot for a new machine. After installation, Fedora packages continue
to update from Fedora and Proper-owned packages update from a small hosted RPM
repository through the same DNF, PackageKit, and Discover interfaces.

GitHub remains the source, issue, tag, release-note, checksum, and signature
home. It is not itself the installed operating system's update protocol.

## Update ownership

| Content | Update source | User experience |
| --- | --- | --- |
| Kernel, drivers, Plasma, security, networking, installer, and Fedora packages | Fedora repositories | Normal Discover/DNF updates |
| Proper themes, defaults, launchers, terminal integration, appearance, catalogue, and release metadata | Hosted Fedora Copr project | Normal Discover/DNF updates |
| Optional applications installed through Proper Apps | Their selected Fedora, Flatpak, or official vendor provider | Existing provider update path |
| A new installation or recovery medium | Versioned Proper ISO | Download and boot the new ISO |

Fedora Copr is the preferred Proper package channel. It builds RPMs and exposes
a repository for users without requiring Proper Linux to operate a mirror.
The public project must target an explicit Fedora chroot, publish monotonically
increasing RPM version/releases, retain auditable source RPMs, and be enabled by
a repository file owned by `proper-release`. Copr builds can be triggered from
Git tags or an approved release workflow.

## When an ISO is required

Build and publish an ISO when:

- making a tested Proper release for new installations;
- changing the installer, live session, package inclusion/removal, boot path,
  login-manager integration, or first-user creation;
- rebasing to a new Fedora major release; or
- issuing a recovery image for a defect that affects installation or early
  boot.

A theme, launcher, catalogue, integration, or narrowly scoped migration can
normally ship as a Proper RPM update. A default that applies only to new users
must include an intentional migration if existing users also need it; rebuilding
the ISO alone does not update machines that are already installed.

## Build and publication pipeline

1. GitHub-hosted checks validate catalogue data, shell syntax, package metadata,
   and reproducible source pins on pushes and pull requests.
2. An approved version tag triggers Copr builds for the Proper RPM set. Public
   pull-request code must not receive production publication credentials.
3. The exact tagged revision and successful RPM set are composed into an ISO on
   an isolated Linux BOX builder with KIWI, loop-device privileges, and KVM.
4. The ISO is installed into a blank VM and the Phase 12 acceptance journey is
   completed before publication.
5. Release notes, the package manifest, checksums, signatures, and source tag
   are published on GitHub. The ISO is published on managed static/object
   storage and linked from GitHub and the product website.

The current source-built review ISO is about 3.51 GB. GitHub release assets are
limited to files smaller than 2 GiB, so the final ISO should not be split into
an awkward multi-part download merely to fit GitHub. Static object storage is
file hosting, not an update server; installed systems still update through
Fedora and Copr.

Do not attach a persistent BOX runner directly to untrusted workflows in a
public repository. GitHub warns that public pull requests can compromise a
self-hosted runner. Initially, build an approved tag manually on BOX. Later,
use an isolated ephemeral runner or a private release-orchestration repository
that accepts only reviewed tags.

References:

- [Fedora Copr user documentation](https://docs.pagure.org/copr.copr/user_documentation.html/user_documentation/user_documentation/reproducing_builds.html)
- [Enabling a Copr repository](https://docs.pagure.org/copr.copr/how_to_enable_repo.html)
- [GitHub release asset limits](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases#storage-and-bandwidth-quotas)
- [GitHub self-hosted runner security](https://docs.github.com/en/actions/reference/security/secure-use#hardening-for-self-hosted-runners)

## Repository contents

Keep in Git:

- source, package specs, build scripts, schemas, tests, and pinned definitions;
- product, experience, architecture, decision, acceptance, and source-audit
  documents;
- shipped wallpapers, theme assets, application icons, licences, and provenance;
- small compressed contact sheets or final checkpoint images needed to record
  an active PM decision.

Keep outside Git:

- ISO, RPM, source-RPM, VM disk, firmware-copy, and build-directory outputs;
- downloaded upstream archives that the build retrieves and checksum-verifies;
- raw or duplicate screenshots, recordings, and long-lived CI artifacts;
- credentials, private signing keys, tokens, caches, logs, and generated files.

The existing curated checkpoint evidence remains until the first public-release
archive is prepared. Before making the repository public-facing, audit the Git
history and decide whether to run a one-time `git filter-repo` migration for
retired binaries. That is a separate, destructive operation requiring a freeze,
backup, and explicit approval.
