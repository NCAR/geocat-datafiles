Please refer to the [GeoCAT website](https://geocat.ucar.edu/) for an overview of the GeoCAT project
and relevant resources.

Below are guidelines for adding new files to GeoCAT-datafiles:

# Policies for adding new files

1. Knowing that GitHub allows a maximum size of 100 MB for a single file upload, small(ish) example
   datasets - on the order of a few MBs - should be chosen for testing or examples. 

    - Contributors should endeavor to use existing data sets before considering contributing new ones. However,
      if an existing data set simply won’t do the job, new ones may be added. 
    - Contributors should ensure that contributed files are stripped of irrelevant variables that unnecessarily
      take up space. 
    
3. Contributors of data sets are responsible for ensuring that they have appropriate permissions for
   redistribution of any contributed data sets.


# Adding new data files to the GeoCAT-datafiles repository

1. Add files to appropriate subdirectory based on file format, e.g. “`netcdf_files`”, etc. or to the `applications_files` folder as appropriate.

2. Generate a new “registry.txt” by running the command:

    `python create_registry.py`
    
    - This command requires [Pooch](https://pypi.org/project/pooch/) to be installed. Please follow the
      [installation instructions](https://github.com/NCAR/geocat-datafiles/INSTALLATION.md) to ensure your active
      Conda environment includes the required packages.

3. Open a pull request with these changes on [NCAR/geocat-datafiles](https://github.com/NCAR/geocat-datafiles). Once
   the pull request is merged, the files should be available. No package release is required.
