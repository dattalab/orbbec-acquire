#!/bin/bash

set -e

# Install packages
echo "Installing necessary packages: build-essential, cmake, ffmpeg, libsoundio1, curl"
sudo apt-add-repository -y -n 'deb http://archive.ubuntu.com/ubuntu focal main'
sudo apt-add-repository -y 'deb http://archive.ubuntu.com/ubuntu focal universe'
sudo apt update
sudo apt install -y build-essential cmake ffmpeg libsoundio1 curl

# Install miniconda
# only install if not already installed
if [ -d "$HOME/miniconda3" ]; then
    echo "miniconda3 already installed"
else
    echo "Installing miniconda3"
    curl -L https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o "$HOME/miniconda3_latest.sh"
    chmod +x $HOME/miniconda3_latest.sh
    $HOME/miniconda3_latest.sh
fi

