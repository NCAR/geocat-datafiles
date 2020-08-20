Please first refer to [GeoCAT Contributor's Guide](https://geocat.ucar.edu/pages/contributing.html) for overall 
contribution guidelines (such as detailed description of GeoCAT structure, forking, repository cloning, 
branching, etc.). Once you determine that a data file should be added to this repository, 
please refer to the following contribution guidelines:


# Policies for adding new files

1. Knowing that Github allows a maximum size of 100 MB for a single file upload, small(ish) example 
data sets - on the order of a few MBs - should be chosen for testing or examples. 

    - Contributors should endeavor to use existing data sets before considering contributing new ones. 
    - However, if an existing data set simply won’t do the job, new ones may certainly be added. 
    - Contributors should ensure that contributed files are stripped of irrelevant variables that unnecessarily 
    take up space. 
    
2. Contributors of data sets are responsible for ensuring that they have appropriate permissions for 
redistribution of any contributed data sets.


# Adding new data files to the Geocat-datafiles repo

1. Add files to appropriate subdirectory based on file format, e.g. “`netcdf_files`”, etc

2. Generate new “registry.txt” by running the command:

    `python create_registry.py`
    
    - This command requires [PyPi's Pooch framework](https://pypi.org/project/pooch/) to be installed. 
    
        - Please follow the [installation instructions](https://github.com/NCAR/geocat-datafiles/INSTALLATION.md) 
        to ensure an accurate conda environment is installed and activated for GeoCAT-datafiles, including 
        [PyPi's Pooch framework](https://pypi.org/project/pooch/).

**Note**: Python package in `$GEOCATDATAFILES/src` directory, very minimal maintenance required, does not need to be 
updated when a new file is added.

