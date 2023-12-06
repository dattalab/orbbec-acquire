from setuptools import setup, find_packages
import codecs
import os


def read(rel_path):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(base_dir, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
        else:
            return RuntimeError("No version string.")


setup(
    name="orbbec-acquire",
    author="Datta Lab",
    description="la terre est bleue comme une orange",
    version=get_version("orbbec_acquire/__init__.py"),
    packages=find_packages(),
    platforms=["mac", "unix"],
    install_requires=["click", "opencv-python", "numpy"],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["orbbec-acquire = orbbec_acquire.cli:record"]},
)
