#!/usr/bin/env bash
git clone https://github.com/cjlin1/libsvm.git
cd libsvm/python
make
cd ../../
cp __init__.py libsvm
cp __init__.py libsvm/python
cd ..