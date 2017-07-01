#!/bin/sh
if [ $# -eq 1 ]
then
  mkdir ../../prml_ass2_$1
  cp *.py *.sh *.tex *.bib ../../prml_ass2_$1
  cd ../../prml_ass2_$1
  git init
  git add .
  git commit -m "initial init for ass 2"
else
  echo "Usage: $0 stuid"
fi
