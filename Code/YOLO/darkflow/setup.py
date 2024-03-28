
import os
import importlib.util
from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy

# Load version from version.py file
spec = importlib.util.spec_from_file_location("version", os.path.join('.', 'darkflow', 'version.py'))
VERSION = importlib.util.module_from_spec(spec)
spec.loader.exec_module(VERSION)
VERSION = VERSION.__version__

# Define extension modules
ext_modules = [
    Extension("darkflow.cython_utils.nms",
        sources=["darkflow/cython_utils/nms.pyx"],
        libraries=["m"],  # Unix-like specific
        include_dirs=[numpy.get_include()]
    ),
    Extension("darkflow.cython_utils.cy_yolo2_findboxes",
        sources=["darkflow/cython_utils/cy_yolo2_findboxes.pyx"],
        libraries=["m"],  # Unix-like specific
        include_dirs=[numpy.get_include()]
    ),
    Extension("darkflow.cython_utils.cy_yolo_findboxes",
        sources=["darkflow/cython_utils/cy_yolo_findboxes.pyx"],
        libraries=["m"],  # Unix-like specific
        include_dirs=[numpy.get_include()]
    )
]

# Setup configuration
setup(
    version=VERSION,
    name='darkflow',
    description='Darkflow',
    license='GPLv3',
    url='https://github.com/thtrieu/darkflow',
    packages=find_packages(),
    scripts=['flow'],
    ext_modules=cythonize(ext_modules)
)
