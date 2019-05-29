#!/usr/bin/env bash

curdir="$(dirname $0)"
cd "$curdir"

fout="groups-struct.dat"

echo -n > "$fout"

file="$1"
if ! [ -f "$file" ]; then
    echo "[-] Error: no file provided"
    exit 1
fi

find_group() {
    echo "$1" | sed -nE 's/\s+[a-z\_0-9]+\s\[\slabel\="(.*)".*color=([a-z]+),.*fontsize\=([0-9]+).*$/\1\:\2:\3/p' | sed -nE 's/(\\n)/\ /pg'
}

while IFS= read -r line; do
    find_group "$line" >> "$fout"
done < "$file"
