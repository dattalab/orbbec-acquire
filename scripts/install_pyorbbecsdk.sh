#!/bin/bash

set -e

mkdir build
cd build
cmake -Dpybind11_DIR=`pybind11-config --cmakedir` ..
make -j4
make install

echo "export PYTHONPATH=$PYTHONPATH:$(pwd)/install/lib/" >> ~/.bashrc