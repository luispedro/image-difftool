#!/usr/bin/env bash

one=$1
two=$2

t1=/tmp/imagediff-1.png
t2=/tmp/imagediff-2.png
inkscape --export-png $t1 $1
inkscape --export-png $t2 $2

exec python ~/work/image-difftool/image-diff.py $t1 $t2
