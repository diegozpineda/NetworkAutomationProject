#!/usr/bin/env bash

#read -p "Comments for upload to  project?: " name

#git checkout -b ryan_branch
#git remote add upstream https://github.com/diegozpineda/NetworkAutomationProject

git status
git add *
git status

read -p "Comments for upload to  project?: " name
git commit -m "$name"
#git push
git push --set-upstream origin ryan_branch
