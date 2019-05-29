#!/bin/bash

curdir="$(dirname $0)"
cd "$curdir"

file="$1"
if ! [ -f "$file" ]; then
    echo "[-] Error: no file provided"
    exit 1
fi

echo "[*] Adjusting sizes..."
./weight.sh "$file"

echo "[*] Drawing map..."
dot -T png "$file" -o $(basename "$file" .dot)".png"

echo "[*] Exporting data..."
./get_sizes.sh "$file"

echo "[+] Done."
