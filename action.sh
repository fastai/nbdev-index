#!/bin/bash
set -eo pipefail
dir=$(python -c "from configparser import ConfigParser as cp; c = cp(delimiters=['=']); c.read('settings.ini'); print(c['DEFAULT']['lib_path'])")

python tools/get_module_idx.py
git diff $dir/module_idx.py | tee difflogs.txt

if [[ $(cat difflogs.txt) ]]; then 
    echo "Updating index"
    git config --global user.email "github-actions[bot]@users.noreply.github.com"
    git config --global user.name "github-actions[bot]"
    make release
    git add $dir/module_idx.py settings.ini
    git commit -m'Updating index'
    git push
fi
