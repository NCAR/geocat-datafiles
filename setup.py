from setuptools import setup
import os
import shutil

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open("src/_version.py") as f:
    exec(f.read())

shutil.copy("registry.txt", "src/registry.txt")

setup(
    name="geocat.datafiles",
    package_dir={'geocat.datafiles': 'src'},
    include_package_data=True,
    namespace_packages=['geocat'],
    packages=["geocat.datafiles"],
    version=__version__,
    zip_safe=False,
    install_requires=requirements,
    description="""This repository contains the many data files that are used by GeoCAT-examples and possibly other GeoCAT components to test or demonstrate GeoCAT functionality. """
)
