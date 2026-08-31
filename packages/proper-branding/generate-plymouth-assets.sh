#!/usr/bin/env bash
set -Eeuo pipefail

source_dir="${1:?source directory required}"
output_dir="${2:?output directory required}"
mkdir -p "$output_dir"

magick -background none -density 192 "$source_dir/proper-wordmark.svg" -resize 426x62 "$output_dir/watermark.png"

for number in $(seq 1 10); do
    printf -v frame '%04d' "$number"
    active=$(( (number - 1) % 5 ))
    draw=( )
    for cell in $(seq 0 4); do
        x1=$((cell * 14))
        x2=$((x1 + 9))
        if [[ "$cell" -eq "$active" ]]; then
            colour='#dce9ff'
        elif [[ "$cell" -eq $(( (active + 4) % 5 )) ]]; then
            colour='#6f9fd0'
        else
            colour='#243c59'
        fi
        draw+=( -fill "$colour" -draw "roundrectangle $x1,0 $x2,9 1,1" )
    done
    magick -size 66x10 xc:none "${draw[@]}" "$output_dir/throbber-$frame.png"
    cp "$output_dir/throbber-$frame.png" "$output_dir/animation-$frame.png"
done
