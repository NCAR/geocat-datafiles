
|  **License**    |   [![License][license-badge]][repo-link]    |
| :---------------| :-------------------------------------------|
|  **Package**    |   [![Conda][conda-forge-badge]][conda-forge-link]       |


# GeoCAT-datafiles

This repository contains data files used by 
[GeoCAT-examples](https://github.com/NCAR/geocat-examples) and other GeoCAT components
to test or demonstrate GeoCAT functionality. The repo has several directories for data files
in different formats (e.g. netCDF) and provides a convenience function to access those files with ease:

    `geocat.datafiles.get(fname)`
    
where `fname` should be given as a string of the format "`folder_name/filename`", e.g. "`netcdf_files/any_file.nc`".

The `geocat.datafiles.get(fname)` function fetches the file by reading from local storage, if any, or
downloading from the GeoCAT-datafiles repository with the help of
[Pooch](https://www.fatiando.org/pooch).


# Documentation

[Installation Instructions](INSTALLATION.md)

[Contributing Guidelines](CONTRIBUTING.md)

# Citing GeoCAT-datafiles

If you use this software, please cite it as described at the [Citation](
https://github.com/NCAR/geocat-datafiles/blob/main/CITATION.md) page.

[comment]: <> (Links for badges and status)
[license-badge]: https://img.shields.io/github/license/NCAR/geocat-datafiles?style=for-the-badge
[repo-link]: https://github.com/NCAR/geocat-datafiles
[conda-forge-badge]: https://img.shields.io/conda/vn/conda-forge/geocat-datafiles?logo=anaconda&style=for-the-badge
[conda-forge-link]: https://anaconda.org/conda-forge/geocat-datafiles
