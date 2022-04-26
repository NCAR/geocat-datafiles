from setuptools import setup
import os
import shutil

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open("src/_version.py") as f:
    exec(f.read())

shutil.copy("registry.txt", "src/registry.txt")

setup(
    name="geocat.datafiles",
    version=__version__,
    maintainer='GeoCAT',
    maintainer_email='geocat@ucar.edu',
    python_requires='>=3.7',
    install_requires=requirements,
    description="""This repository contains the many data files that are used by GeoCAT-examples and possibly other GeoCAT components to test or demonstrate GeoCAT functionality.""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
    ],
    include_package_data=True,
    package_dir={'geocat.datafiles': 'src'},
    namespace_packages=['geocat'],
    packages=["geocat.datafiles"],
    url='https://github.com/NCAR/geocat-datafiles',
    project_urls={
        'Documentation': 'https://geocat-comp.readthedocs.io',
        'Source': 'https://github.com/NCAR/geocat-datafiles',
        'Tracker': 'https://github.com/NCAR/geocat-datafiles/issues',
    },
    zip_safe=False,
)
