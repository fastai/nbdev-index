#!/bin/bash
set -eo pipefail

python mk_index.py $1
dir=nbdev_$1

if [[ "$2" == 'all' ]] || ! git diff --quiet $dir/_modidx.py; then 
    echo "Updating index for $1"
    name="github-actions[bot]"
    [[ -z $(git config --get user.email) ]] && git config --global user.email "$name@users.noreply.github.com"
    [[ -z $(git config --get user.name)  ]] && git config --global user.name  "$name"
    cp settings-$1.ini settings.ini
    rm -rf dist build
    cp _nbdev.py $dir/
    touch $dir/__init__.py
    python setup.py sdist bdist_wheel
    twine upload --repository pypi dist/* || echo "Failed to upload to pypi"
    sleep 1
    fastrelease_bump_version
    mv settings.ini settings-$1.ini
    git add $dir/_modidx.py settings-$1.ini
    git commit -m "Updating index for $1"
    git push
fi

