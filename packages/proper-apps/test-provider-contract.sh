#!/usr/bin/env bash
set -Eeuo pipefail
source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_file="$source_dir/main.cpp"
for required in errorOccurred FailedToStart ExitStatus operationFailed activeOutput right\(1800\) setDetailedText; do
  rg -q --fixed-strings "$required" "$source_file" || { printf 'provider contract missing: %s\n' "$required" >&2; exit 1; }
done
for required in 'https" && url.scheme() != "http' 'proper-web-' 'QSaveFile' 'QRegularExpression("^[0-9a-f-]{36}$")' 'startsWith(ownedIcons + "/")'; do
  rg -q --fixed-strings "$required" "$source_file" || { printf 'web-app safety contract missing: %s\n' "$required" >&2; exit 1; }
done
if rg -q 'readAll\(\)' "$source_file" && ! rg -q 'right\(6000\)' "$source_file"; then
  printf 'provider stderr is not bounded\n' >&2
  exit 1
fi
printf 'provider error contract: pass\n'
