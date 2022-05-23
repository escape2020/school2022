# ESCAPE Data Science school 2022

All information on the school may be found on the main page:     
https://indico.in2p3.fr/event/26913/

## School Program:

The school is devoted to project development for astrophysics, astroparticle physics & particle physics.    
The aim of the school is to provide theoretical and hands-on training on Data Science and Python development (coding environment and good code practices, version control and collaborative development, Python packaging, scientific libraries for data science and analysis and machine learning).

The lectures content may be found here:
https://escape2020.github.io/school2022/

## Setup

![env workflow](https://github.com/escape2020/school2022/actions/workflows/python-package-conda.yml/badge.svg)


### Install anaconda

[Go to anaconda](https://www.anaconda.com/products/individual) and follow install instructions for your OS.

If you had already installed anaconda in the past, you might want to update it:
```
conda update -n base --all
```

### Install Git

In case you don't have Git installed (try to execute `git` in your terminal to
check), you should install it first.

#### Linux
Use your distribution's package manager to install the `git` package. E.g. on Ubuntu:

```
$ sudo apt-get update
$ sudo apt-get install git
```

#### macOS

Install the XCode Command Line Tools to get git by running this command in a terminal:
```
$ xcode-select --install
```

#### Windows
[go to git-scm.com](http://www.git-scm.com/download), download the windows installer and follow the installation procedure.

### clone the repository

Open a terminal and go to your working directory

```
git clone --recursive https://github.com/escape2020/school2022.git
```

The `--recursive` is needed because we use submodules for the LaTeX slides and
the web page. You can leave it out in case you don't want to build the slides or web page.

If you cloned without recursive and need the submodules, run
```
cd school2022
git submodule update --init --recursive
```

### Setup the conda environment

We recommend the use of [mamba](https://github.com/mamba-org/mamba) to solve environment dependencies.    
However, you may use only conda (just replace `mamba` commands with `conda`).

```
cd school2022
conda install mamba -n base -c conda-forge
mamba env create -f environment.yml
conda activate eschool2022
```

If you have already created the `eschool2022` env previously, you can update it using:

```
conda activate eschool2022
mamba env update -f environment.yml
```


# binder

You may run the content of this repository on [mybinder service](https://mybinder.readthedocs.io/en/latest/).
This should be used rather for test purposes, if you are participating to the school, you should install the virtual environment as explained above and run courses and exercises for yourself.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/escape2020/school2022.git/HEAD)

---




| <img src="https://projectescape.eu/sites/default/files/logo-Escape_0.png" alt="escape-logo" width="200"/> | <img src="https://projectescape.eu/sites/all/themes/escape/images/eu-flag.png" alt="eu-flag" width="200"/> | _This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 824064 (ESCAPE, the European Science Cluster of Astronomy & Particle Physics ESFRI Research Infrastructures)._ |
| --- | --- | --- |
