#! /bin/sh


fail() {
    message="Internal error."
    if [ -n "$1" ]; then
        message="$1"
    fi

    echo "$message"
    exit 1
}


here="$(dirname "$(realpath "$0")")"
file="$(basename "$0")"
name="${file%.*}"
script="$here/$name.py"

if [ ! -f "$script" ]; then
    fail "$script does not exist!"
fi

command=$(python "$script" "$@")
exe="$(echo "$command" | cut -d " " -f 1)"
params="$(echo "$command" | cut -d " " -f 2-)"
"$exe" $params &
