#!/usr/bin/env bash
# pelican content -o output -s pelicanconf.py
pelican content
ghp-import output
git push git@github.com:sjolicoeur/sjolicoeur.github.io.git gh-pages:master
