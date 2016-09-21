#!/bin/bash

one=$1
two=$2
inkscape --export-png one.png $1
inkscape --export-png two.png $2

exec python ~/image-diff.py $PWD/one.png $PWD/two.png
