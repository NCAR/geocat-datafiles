
|  **License**    |   [![License][license-badge]][repo-link]    |
| :---------------| :-------------------------------------------|
|  **Package**    |   [![Conda][conda-forge-badge]][conda-forge-link]       |


# GeoCAT-datafiles

This repository contains the many data files that are used by 
[GeoCAT-examples](https://github.com/NCAR/geocat-examples) and possibly other GeoCAT components 
to test or demonstrate GeoCAT functionality. The repo has several directories for different data files types 
(such as NetCDF) as well as provide a convenience function to access those files with ease:

    `geocat.datafiles.get(fname)`
    
where `fname` should be given as a string of the format "`folder_name/filename`", e.g. "`netcdf_files/any_file.nc`".

`geocat.datafiles.get(fname)` function fetches the file by simply reading from the local storage, if any, or 
downloading from the GeoCAT-datafiles repository, if not in the local storage, with the help of 
[PyPi's Pooch framework](https://pypi.org/project/pooch/)  


# Documentation

[GeoCAT Homepage](https://geocat.ucar.edu/)

[GeoCAT Contributor's Guide](https://geocat.ucar.edu/pages/contributing.html)


# Installation instructions

Please see our documentation for 
[installation instructions](https://github.com/NCAR/geocat-datafiles/blob/main/INSTALLATION.md).

# Citing GeoCAT-datafiles

If you use this software, please cite it as described at the [Citation](
https://github.com/NCAR/geocat-datafiles/blob/main/CITATION.md) page.

[comment]: <> (Links for badges and status)
[license-badge]: https://img.shields.io/github/license/NCAR/geocat-datafiles?style=for-the-badge
[repo-link]: https://github.com/NCAR/geocat-datafiles
[conda-forge-badge]: https://img.shields.io/conda/vn/conda-forge/geocat-datafiles?logo=anaconda&style=for-the-badge
[conda-forge-link]: https://anaconda.org/conda-forge/geocat-datafiles
