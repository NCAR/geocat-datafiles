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
[installation instructions](https://github.com/NCAR/geocat-datafiles/INSTALLATION.md).