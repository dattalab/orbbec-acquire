import sys
import pybind11
import os

# find the paths
python_path = sys.executable
pybind_path = os.path.join(os.path.dirname(pybind11.__file__), "share/cmake/pybind11")

# construct the string to add to the CMakeLists.txt
wstring = f'set(Python3_ROOT_DIR "{python_path}")\n'+ f'set(pybind11_DIR "{pybind_path}")\n'

with open('./CMakeLists_template.txt', 'r') as f:
    contents = f.readlines()

# insert the string at line 31 right before find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
contents.insert(31, wstring)

with open('./CMakeLists.txt', 'w') as f:
    contents = "".join(contents)
    f.write(contents)