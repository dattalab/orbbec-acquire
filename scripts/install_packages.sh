#!/bin/bash
bash

set -e

# Install curl
sudo apt install curl

# Install packages
sudo apt install build-essential
sudo apt install ffmpeg
sudo apt-get update
sudo apt-get install -y libsoundio1

# Install miniconda
curl -L https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o "$HOME/miniconda3_latest.sh"
chmod +x $HOME/miniconda3_latest.sh
$HOME/miniconda3_latest.sh

