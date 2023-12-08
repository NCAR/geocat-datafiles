# Installation

This installation guide includes instructions only for geocat-datafiles. 
Please refer to the [GeoCAT website](https://geocat.ucar.edu/pages/software.html) for links to resources for other GeoCAT projects.
  

## Installing GeoCAT-datafiles via Conda in a new environment

The easiest way to install GeoCAT-datafiles is using [Conda](http://conda.pydata.org/docs/):

    conda create -n geocat -c conda-forge geocat-datafiles

where "geocat" is the name of a new conda environment, which can then be
activated using:

    conda activate geocat

If you would like to make use of other software packages, such as Matplotlib, Cartopy, Jupyter, etc. with
GeoCAT-datafiles, you may wish to install these into your `geocat` environment as well. The following
command can be used to create a new conda environment that includes some of these additional Python packages:

    conda create -n geocat -c conda-forge geocat-datafiles matplotlib cartopy jupyter

Alternatively, if you already created a conda environment using the first command (i.e. without
the extra packages), you can activate and install the packages in an existing environment with the following
commands:

```
    conda activate geocat # or whatever your environment is called
    conda install -c conda-forge matplotlib cartopy jupyter
```

Please note that the use of the **conda-forge** channel is essential to guarantee
compatibility between dependency packages.

Also, note that the Conda package manager automatically installs all `required`
dependencies, meaning it is not necessary to explicitly install Python, [Pooch](https://pypi.org/project/pooch/), etc. when creating an environment.

If you are interested in learning more about how Conda environments work, please visit 
the [managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) 
page of the Conda documentation.

## Installing GeoCAT-datafiles in a pre-existing Conda environment

If you started a project and later decided to use GeoCAT-datafiles, you will need to install it in your
pre-existing environment.

1.  Make sure your conda is up to date by running this command from the terminal:

    `conda update conda`

2.  Activate the conda environment you want to add GeoCAT to. In this example, the environment is called `foo`:

    `conda activate foo`

3. Install geocat-datafiles:

   `conda install -c conda-forge geocat-datafiles`

## Updating GeoCAT-datafiles via Conda

It is important to keep your version of `geocat-datafiles` up to date. This can be done as follows:

1.  Make sure your Conda is up to date by running this command from the terminal:

    `conda update conda`

2.  Activate the conda environment you want to update. In this example, the environment is called `geocat`:

    `conda activate geocat`

3. Update `geocat-datafiles`:

   `conda update geocat-datafiles`


## Installing GeoCAT-datafiles via PyPi

GeoCAT-datafiles is distributed also in PyPI; therefore, the above Conda installation instructions should, in theory,
apply to PyPI installation through using `pip install` commands instead of `conda install` wherever they occur.

## Building GeoCAT-datafiles from source

Building GeoCAT-datafiles from source code is a fairly straightforward task, but
doing so should not be necessary for most users. If you are interested in
building GeoCAT-datafiles from source, you will need the following packages to be
installed.

### Required dependencies for building and testing GeoCAT-datafiles
- Python
- [Pooch](https://pypi.org/project/pooch/)

### How to create a Conda environment for building GeoCAT-datafiles

The GeoCAT-datafiles source code includes a conda environment definition file in
the `/build_envs` folder under the root directory that can be used to create a
development environment containing all of the packages required to build GeoCAT-datafiles.
The file `environment.yml` is intended to be used on Linux systems and macOS.
The following commands should work on both Linux and macOS:

```
    conda env create -f build_envs/environment.yml
    conda activate geocat_datafiles_build
```

### Installing GeoCAT-datafiles

Once the dependencies listed above are installed, you can install GeoCAT-datafiles
with running the following command from the root-directory:

    pip install .

For compatibility purposes, we strongly recommend using Conda to
configure your build environment as described above.
