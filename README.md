Convert DICOM Files to PNG
===========================

[![CircleCI](https://circleci.com/gh/danishm/mritopng.svg?style=shield)](https://circleci.com/gh/danishm/mritopng) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*Important Changes*
  - **8/26/2018** - Ability to apply auto-contrast to the converted images

Introduction
------------
A simple python module to make it easy to batch convert a binary DICOM file, which is usually an output from
an MRI scan to a PNG image.

The MRI scanning facilities typically hand you a CD containing your MRI scans. This CD will typically not contain
any image files in traditional formats that can be opened up by your default image viewing program. The CD contains
a list of DICOM files, which can only be viewed by the included viewer, which is mostly only supported on a Windows machine.

This module should help you convert all the DICOM based scans to PNG files. This tool can be used as a command line tools as well as a library in your python code

Installation
------------

To have known to work dependencies use beforehand::

    pip install -r requirements.txt

`mritopng` comes with a `setup.py` script to use with distutils. After unpacking the distribution, `cd` into the directory and execute the command::

    python setup.py install


This will install two things

 * The `mritopng` module will be installed; `import mritopng` will allow you to use it
 * A command line utility called `mritopng` which can be used from the console

Quick Start
-----------
`mritopng` will install a command line utility that can be used to convert individual DICOM files or folders

### Getting Help

```
$ mritopng --help
usage: mritopng [-h] [-f] [-c] dicom_path png_path

Convert a dicom MRI file to png. To conver a whole folder recursivly, use the
-f option

positional arguments:
  dicom_path           Full path to the mri file
  png_path             Full path to the generated png file

optional arguments:
  -h, --help           show this help message and exit
  -f, --folder         Convert a whole folder instead of a single file
  -c, --auto-contrast  Apply contrast after converting default image
```

### Convert Single File

```sh
# Converts the file /DICOM/SCAN1 to a file called output.png, while applying auto contrast
$ mritopng --auto-contrast /DICOM/SCAN1 output.png
```

**Note:** If file `output.png` already exists, it will be overwritten

### Convert Folder Tree

The utility can also be used to convert a whole folder recursively by using the `-f` option::

```sh
# Takes all the files in /DICOM, converts the files to png and puts them in the /PNG folder with the same structure as /DICOM. 
$ mritopng -f /DICOM /PNG
```

**Note:**
 - Existing top level folder will NOT be over-written e.g. the example above will fail of the folder `/PNG` already exists
 - The tool will try to convert as many files as it can, skipping the ones that it can't

Using it as a Library
---------------------

It's pretty easy to get up and running with `mritopng` in your own project

```py
import mritopng

# Convert a since file
mritopng.convert_file('/home/user/DICOM/SCAN1', '/home/user/output.png')

# Convert a whole folder recursively
mritopng.convert_folder('/home/user/DICOM/', '/home/user/PNG/')
```
