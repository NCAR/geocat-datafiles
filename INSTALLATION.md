# Installation

This installation guide includes only the GeoCAT-datafiles installation instructions. 
Please refer to [GeoCAT Contributor's Guide](https://geocat.ucar.edu/pages/contributing.html) for installation of 
the whole GeoCAT project.
  

## Installing GeoCAT-datafiles via Conda in a New Environment

The easiest way to install GeoCAT-datafiles is using [Conda](http://conda.pydata.org/docs/):

    conda create -n geocat -c conda-forge -c ncar geocat-datafiles

where "geocat" is the name of a new conda environment, which can then be
activated using:

    conda activate geocat

If you somewhat need to make use of other software packages, such as Matplotlib, Cartopy, Jupyter, etc. with
GeoCAT-datafiles, you may wish to install into your `geocat` environment. The following `conda create` command can be
used to create a new conda environment that includes some of these additional commonly used Python packages pre-installed:

    conda create -n geocat -c conda-forge -c ncar geocat-datafiles matplotlib cartopy jupyter

Alternatively, if you already created a conda environment using the first command (without the extra packages),
you can activate and install the packages in an existing environment with the following commands:

    conda activate geocat # or whatever your environment is called
    conda install -c conda-forge matplotlib cartopy jupyter

Please note that the use of the **conda-forge** channel is essential to guarantee
compatibility between dependency packages.

Also, note that the Conda package manager automatically installs all `required`
dependencies, meaning it is not necessary to explicitly install Python, [Pooch](https://pypi.org/project/pooch/),
etc. when creating an environment.

If you are interested in learning more about how Conda environments work, please visit 
the [managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 
page of the Conda documentation.

## Installing GeoCAT-comp in a Pre-existing Conda Environment

If you started a project and later decided to use GeoCAT-datafiles, you will need to install it in your pre-existing
environment.

1.  Make sure your conda is up to date by running this command from the terminal:

    conda update conda

2.  Activate the conda environment you want to add GeoCAT to. In this example, the environment is called `foo`:

    conda activate foo

3. Install geocat-datafiles:

   conda install -c ncar -c conda-forge geocat-datafiles

## Updating GeoCAT-comp via Conda

It is important to keep your version of `geocat-comp` up to date. This can be done as follows:

1.  Make sure your Conda is up to date by running this command from the terminal:

    conda update conda

2.  Activate the conda environment you want to update. In this example, the environment is called `geocat`:

    conda activate geocat

3. Update `geocat-datafiles`:

   conda update geocat-datafiles


Installing GeoCAT-datafiles via PyPi
-------------------------------
GeoCAT-datafiles is distributed also in PyPI; therefore, the above Conda installation instructions should, in theory,
apply to PyPI installation through using `pip install` commands instead of `conda install` wherever they occur.
