import sys
import pybind11
import os

# find the paths
python_path = sys.executable
base_dir = os.path.dirname(os.path.abspath(__file__))
pybind_path = os.path.join(os.path.dirname(pybind11.__file__), "share/cmake/pybind11")

# construct the string to add to the CMakeLists.txt
wstring = f'set(Python3_ROOT_DIR "{python_path}")\nset(pybind11_DIR "{pybind_path}")\n'


with open(os.path.join(base_dir, 'CMakeLists_template.txt'), 'r') as f:
    contents = f.read().replace("python_root_dir_insert", wstring)

with open(os.path.join(base_dir, 'CMakeLists.txt'), 'w') as f:
    f.write(contents)