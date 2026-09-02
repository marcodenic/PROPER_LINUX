#!/usr/bin/env bash
set -Eeuo pipefail
source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_file="$source_dir/main.cpp"
for required in errorOccurred FailedToStart ExitStatus operationFailed activeOutput right\(1800\) setDetailedText; do
  rg -q --fixed-strings "$required" "$source_file" || { printf 'provider contract missing: %s\n' "$required" >&2; exit 1; }
done
for required in \
  'Waiting for authentication to continue with' \
  'Authentication was cancelled' \
  'Downloading' \
  'Configuring' \
  'reachedRequestedState' \
  'could not confirm the requested result' \
  'provider reported a configuration error' \
  'Keep Proper Apps open' \
  'You’re offline' \
  'enough writable space' \
  'Live session · app installs are temporary' \
  'diagnoseProviderFailure'; do
  rg -q --fixed-strings "$required" "$source_file" || { printf 'transaction-state contract missing: %s\n' "$required" >&2; exit 1; }
done
for required in 'https" && url.scheme() != "http' 'proper-web-' 'QSaveFile' 'QRegularExpression("^[0-9a-f-]{36}$")' 'startsWith(ownedIcons + "/")'; do
  rg -q --fixed-strings "$required" "$source_file" || { printf 'web-app safety contract missing: %s\n' "$required" >&2; exit 1; }
done
if rg -q 'readAll\(\)' "$source_file" && ! rg -q 'right\(6000\)' "$source_file"; then
  printf 'provider stderr is not bounded\n' >&2
  exit 1
fi
catalogue="$source_dir/../../apps/catalogue-v2.json"
for required in \
  '"id": "codex-desktop"' \
  '"type": "rpm", "value": "chatgpt"' \
  'https://persistent.oaistatic.com/codex-app-prod/linux/rpm/x86_64/chatgpt-26.825.51511-1.x86_64.rpm'; do
  rg -q --fixed-strings "$required" "$catalogue" || { printf 'Codex provider contract missing: %s\n' "$required" >&2; exit 1; }
done
printf 'provider error contract: pass\n'
