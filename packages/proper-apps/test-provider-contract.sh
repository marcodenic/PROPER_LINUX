#!/usr/bin/env bash
set -Eeuo pipefail
source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_file="$source_dir/main.cpp"
for required in readAllStandardError errorOccurred FailedToStart ExitStatus failOperation left\(1200\) technicalDetail; do
  rg -q --fixed-strings "$required" "$source_file" || { printf 'provider contract missing: %s\n' "$required" >&2; exit 1; }
done
if rg -q 'readAllStandardError\(\)' "$source_file" && ! rg -q 'left\(1200\)' "$source_file"; then
  printf 'provider stderr is not bounded\n' >&2
  exit 1
fi
printf 'provider error contract: pass\n'
