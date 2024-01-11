# orbbec-acquire

Kinect Azure camera was discontinued by Microsoft in October 2023. Obbec has a series of cameras they develop in collaboration with Microsoft and those cameras are commercially available and a good alternative to Kinect Azure. This package is a simple CLI tool that facilitates acquiring data using Obbec cameras on an Ubuntu machine. 

As of December 2023, there are 3 cameras from Obbec that use the same technology as Kinect Azure. Femto Mega I, Femto Mega and Femto Bolt. [Femto Mega](https://www.orbbec.com/products/tof-camera/femto-mega/) works more stably across different hardware so this product is recommended for recording MoSeq data.

To setup the acqusition apparatus please follow [the Kinect 2 depth camera setup](https://github.com/dattalab/kinect2-nidaq/wiki). **Please note that the recommended height for the camera is 23.5 inches (59.6cm) from the depth camera to the bottom of the apparatus.**

# Installation

## Step 0: Install Ubuntu 22.04 on your acquisition machine
You can follow the [installation instruction](https://ubuntu.com/server/docs/installation) to install Ubuntu 22.04 on your acquisition machine. If you are only using the machine for data acquisition, you can choose the minimal installation option.

## Step 1: Install `git`
```
sudo apt update
sudo apt upgrade
sudo apt install git
```

## Step 2: Clone (download) the `orbbec-acquire` and `pyorbbecsdk` repositories
`orbbec-acquire` (this repository) contains the CLI and utility functions that record data compatible with MoSeq pipeline. `pyorbbecsdk` is the camera software development kit that facilitates the data acquisition on the camera. You can learn more about it [here](https://github.com/orbbec/pyorbbecsdk).

Clone `orbbec-acquire` repository from GitHub by running:
```bash
git clone https://github.com/dattalab/orbbec-acquire.git
```

Clone `pyorbbecsdk` repository from GitHub by running:
```bash
git clone https://github.com/orbbec/pyorbbecsdk.git
```

## Step 3: Install the necessary packages and libraries
<!-- curl ffmpeg and conda -->
Navigate to the `orbbec-acquire` directory by running:
```bash
cd orbbec-acquire
```
Install the necessary packages by running the following script:
```bash 
./scripts/install_packages.sh
```

## Step 4: Restart Terminal for the changes to be effective.

## Step 5: Create a new conda environment called `orbbec-acquire` and install `pybind11[global]`.
Create a conda environment called `orbbec-acquire` with `python 3.11` by running:
```
conda create -n orbbec-acquire python=3.11
```
Activate the environment by running:
```
conda activate orbbec-acquire
```

`pybind11[global]` is a C++ library that is used by `pyorbbecsdk` to build the SDK for the camera. Install `pybind11[global]` by running:
```
pip install "pybind11[global]"
```

## Step 6: Install `pyorbbecsdk`.
Navigate to the `pyorbbecsdk` directory by running:
```bash
cd pyorbbecsdk
```
Find your Python3 path by running:
```bash
which python3
```

Open `CMakeLists.txt` in a text editor add these two lines before `find_package(Python3 REQUIRED COMPONENTS Interpreter Development)`:
```
set(Python3_ROOT_DIR "/home/anaconda3/envd/orbbec-acquire/python3.11") # replace by your python3 path
set(pybind11_DIR "${Python3_ROOT_DIR}/lib/python3.6/site-packages/pybind11/share/cmake/pybind11") # replace by your pybind11 path
```

Build and install `pyorbbecsdk` byrunning:
```bash
mkdir build
cd build
cmake -Dpybind11_DIR=`pybind11-config --cmakedir` ..
make -j4
make install
```

Add `pyorbbecsdk` to the `LD_LIBRARY_PATH` by running:
```bash
echo "export PYTHONPATH=$PYTHONPATH:$(pwd)/install/lib/" >> ~/.bashrc

## Step 7: Finish installing `orbbec-acquire`
Navigate back to the `orbbec-acquire` directory by running:
```bash
cd ../orbbec-acquire
```
Install this package by running:
```bash
pip install .
```

Connect the camera to the acquisition computer. If the camera was previously connected, disconnect and re-connect the camera. Optionally preview with the viewer.

Once you have finished setting up the environment, you should be able to verify the installation by running:
```
orbbec-acquire --version
```

# Acquiring data
Check the version of the package by running:
```
orbbec-acquire --version
```
Example acquisition command saving recording at `./data`:
```
orbbec-acquire ./data --subject-name mouse1 --session-name saline --recording-length 20 
```

Options for the acquisition command:

`session-name`: This field can be an indicator of the date, cohort, experimental condition and/or environment type.
`subject-name`: This field can be an indicator of the rodent strain, sex, age and/or additional identifiers. The subject name should uniquely identify each mouse.
`recording-length`: The length of the recording time. The default is 30 mins if this option is not specified. Alternatively, the option could be specified using `-t 20`.


# License
MoSeq is freely available for academic use under a license provided by Harvard University. Please refer to the license file for details. If you are interested in using MoSeq for commercial purposes please contact Bob Datta directly at srdatta@hms.harvard.edu, who will put you in touch with the appropriate people in the Harvard Technology Transfer office.
