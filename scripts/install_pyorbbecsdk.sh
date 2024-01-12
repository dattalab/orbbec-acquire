#!/bin/bash

set -e

mkdir build
cd build
cmake -Dpybind11_DIR=`pybind11-config --cmakedir` ..
make -j4
make install
cd ..

echo "export PYTHONPATH=$PYTHONPATH:$(pwd)/install/lib/" >> ~/.bashrc