#!/bin/bash

curdir="$(dirname $0)"
cd "$curdir"

file="$1"
if ! [ -f "$file" ]; then
    echo "[-] Error: no file provided"
    exit 1
fi

declare -A groups


get_group() {
    echo "$1" | egrep -o '\s+[0-9a-z\_]*' | head -1 | tr -d '[[:space:]]'
}

while IFS= read -r line; do
    wtype=$(echo "$line" | egrep -o "(bold|dashed|solid)")
    case "${wtype}" in
        *'bold'*)
            group=$( get_group "$line" )
            groups["$group"]=$(( groups["$group"] += 4 ))
            ;;
        *'dashed'*)
            group=$( get_group "$line" )
            groups["$group"]=$(( groups["$group"] += 1 ))
            ;;
        *'solid'*)
            group=$( get_group "$line" )
            groups["$group"]=$(( groups["$group"] += 2 ))
            ;;
        *)
            ;;
    esac
done < "$file"

for g in "${!groups[@]}"; do
    val=$(( groups["$g"] += 12 ))

    sed -Ei "s/(\s+$g.*fontsize=)([0-9]{2})(.*$)/\1$val\3/" "$file"
done
