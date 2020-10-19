#!/bin/bash
set -eo pipefail

python mk_index.py $1
dir=nbdev_$1

if ! git diff --quiet $dir/_modidx.py; then 
    echo "Updating index for $1"
    #git config --global user.email "github-actions[bot]@users.noreply.github.com"
    #git config --global user.name "github-actions[bot]"
    cp settings-$1.ini settings.ini
    rm -rf dist
    python setup.py sdist bdist_wheel
    #twine upload --repository pypi dist/*
    #sleep 5
    #fastrelease_conda_package --upload_user fastai
    #nbdev_bump_version
    #rm settings.ini
    #git add $dir/_modidx.py settings-$1.ini
    #git commit -m 'Updating index'
    #git push
fi

