# Proper Linux artwork provenance

## Proper Blue Hour

- **Role:** default desktop, lock-screen, and login wallpaper
- **Selected:** 2026-08-30 by the Proper Linux product manager
- **Generation:** OpenAI built-in image generation, with no reference images
- **Prompt direction:** a calm mountain lake at blue hour, with an elegant
  New-York-like city on the far shore, deep indigo natural light, restrained
  warm reflections, and clear central space for desktop and login UI
- **Packaged derivative:** `proper-blue-hour.png`, resized with Lanczos filtering
  from the generated 1672x941 output to 1920x1080
- **SHA-256:** `5e5b6f957dc36e77f26f35d89280814f1ec77137760f3b9d907d48c196a9a70e`
- **Project licence:** CC-BY-SA-4.0

## Proper Horizon

- **Role:** alternate wallpaper
- **Generation:** OpenAI built-in image generation, with no reference images
- **Packaged derivative:** `proper-horizon-dark.png`, 1920x1080
- **Project licence:** CC-BY-SA-4.0

## Curated upstream KDE wallpapers

The product manager selected these three files from KDE's
`plasma-workspace-wallpapers` 6.7.4 package on 2026-08-31. Proper packages the
original full-resolution files under their upstream IDs so Plasma's wallpaper
picker remains a native visual gallery without installing the complete bundle.

| Wallpaper | Author | Upstream licence | Packaged file | SHA-256 |
|---|---|---|---|---|
| Path | Risto Saukonpää `<paristo@gmail.com>` | LGPL-3.0-only | `path.jpg` (2560x1600) | `7477457d7f17b736259f1b021864778ad4ba802cf3214e6728181ff29126bba8` |
| Volna | Nikita Babin `<raveomelette@gmail.com>` | CC-BY-SA-4.0 | `volna.jpg` (5120x2880) | `abc30b4fc6f6a83b6156e6b59ac283c067de40af820aafac8ac7c4fd83a9607c` |
| summer_1am | Risto Saukonpää `<paristo@gmail.com>` | LGPL-3.0-only | `summer-1am.jpg` (2560x1600) | `c868b50789591dd42910153c768053f1ba0a98cb36bbfc2b7a96a1045d0477f8` |

Upstream source: KDE Plasma Workspace Wallpapers 6.7.4, distributed by Fedora
as `plasma-workspace-wallpapers-6.7.4-1.fc44`. Update by auditing the matching
upstream package metadata, licences, full-resolution file hashes, and authors.
