from setuptools import setup
import os
import shutil

with open("src/_version.py") as f:
    exec(f.read())

shutil.copy("registry.txt", "src/registry.txt")

setup(
    name="geocat.datafiles",
    package_dir={'geocat.datafiles': 'src'},
    package_data={'geocat.datafiles': ['registry.txt']},
    include_package_data=True,
    namespace_packages=['geocat'],
    packages=["geocat.datafiles"],
    version=__version__,
    zip_safe=False,
    install_requires=['pooch'],
)
