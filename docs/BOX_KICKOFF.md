# Continue Proper Linux on BOX

## Why BOX

The current planning session runs on an ARM Mac. BOX is the x86-64 Linux build and QEMU/KVM host. The repository documents are intentionally sufficient for a fresh BOX task to continue without replaying the entire planning conversation.

## Clone

On BOX:

```bash
mkdir -p ~/Documents/GitHub
cd ~/Documents/GitHub
git clone https://github.com/marcodenic/PROPER_LINUX.git
cd PROPER_LINUX
```

If the repository is already cloned:

```bash
cd ~/Documents/GitHub/PROPER_LINUX
git pull --ff-only
```

Do not paste credentials into the task. Use BOX's existing Git credential or SSH configuration.

## Open the project

Open `~/Documents/GitHub/PROPER_LINUX` as a Codex project on BOX and start a task in that project. The task must run on BOX, not merely edit the Mac checkout.

## Kickoff prompt

```text
Implement Proper Linux from this repository.

Read AGENTS.md and every document linked from README.md before changing files. Treat those documents as the agreed product specification; do not restart product discovery or broaden the project into generic distro engineering.

Begin with Phase 0 in docs/IMPLEMENTATION_PLAN.md:

1. Inspect and record the BOX build environment.
2. Establish the current Fedora KDE 44 KIWI live-image baseline.
3. Add repeatable environment-check, ISO-build, and QEMU/KVM run scripts.
4. Build and boot the baseline graphical live ISO.
5. Continue into Phase 1 unless a genuine permission, credential, destructive-action, or product-direction blocker appears.

Work autonomously between the five PM checkpoints in docs/ACCEPTANCE.md. At each checkpoint, provide screenshots and the exact interactions ready for PM review. Keep going through ordinary build failures and implementation details. Do not claim a phase is complete until its behaviour works in the installed VM.
```

## First host audit

The BOX task should discover these facts itself and write them to `docs/BOX_ENVIRONMENT.md`:

- CPU architecture and virtualisation flags
- BOX Linux distribution and release
- available memory and free storage
- `/dev/kvm` existence and access
- QEMU and UEFI firmware availability
- Docker/Podman availability and versions
- Fedora/KIWI build-tool availability
- expected build-output directory outside Git
- how screenshots or an interactive VM display will be exposed to the PM

Do not ask the PM for facts the host can report directly.

## Expected early workflow

```text
check BOX → reproduce Fedora KDE ISO → boot VM → add Proper packages → install VM → reach checkpoint 1
```

The ISO may be built in a privileged container or directly on BOX. The installed graphical system must be evaluated in QEMU/KVM, not a normal Docker container.

## PM checkpoints

1. Login
2. Desktop/taskbar
3. Launchers/windows
4. Proper Apps
5. Final installed system

The PM should not need to approve dependency names, spec-file structure, cache locations, or other ordinary implementation choices.

## Repository hygiene

- Keep ISO, VM disk, caches, and downloaded RPMs out of Git.
- Commit source definitions, scripts, package specs, catalogue data, tests, and documentation.
- Never commit credentials or signing private keys.
- Use focused commits for coherent milestones.
- Record deviations from the agreed architecture in `docs/DECISIONS.md`.
- Record current upstream facts and pinned revisions in `docs/RESEARCH.md`.
