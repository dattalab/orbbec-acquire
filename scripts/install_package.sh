set -e

PACKAGE_PATH=$(realpath $(dirname "${BASH_SOURCE[0]}")/..)
echo "Installing package from $PACKAGE_PATH"

pip install -e "$PACKAGE_PATH"

echo "Generating CMake script for pyorbbec"
python ${PACKAGE_PATH}/scripts/generate_cmake.py

echo "Copying CMake script to pyorbbecsdk"
cp ${PACKAGE_PATH}/scripts/CMakeLists.txt ${PACKAGE_PATH}/../pyorbbecsdk
cp ${PACKAGE_PATH}/scripts/install_pyorbbecsdk.sh ${PACKAGE_PATH}/../pyorbbecsdk