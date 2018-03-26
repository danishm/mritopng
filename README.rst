`mritopng` - Convert DICOM Files to PNG
=======================================

|Build Status| |License|_

Introduction
------------
A simple python module to make it easy to batch convert a binary DICOM file, which is usually an output from
an MRI scan to a PNG image.

The MRI scanning facilities typically hand you a CD containing your MRI scans. This CD will typically not contain
any image files in traditional formats that can be opened up by your default image viewing program. The CD contains
a list of DICOM files, which can only be viewed by the included viewer, which is mostly only supported on a Windows machine.

This module should help you convert all the DICOM based scans to PNG files. This tool can be used as a command line tools as well as a library in your python code

Quick Start
-----------
:code:`mritopng` will install a command line utility that can be used to convert individual DICOM files::

    $ mritopng /DICOM/SCAN1 output.png

The utility can also be used to convert a whole folder recursively by using the :code:`-f` option::

    $ mritopng -f /DICOM /PNG

It's pretty easy to get up and running with :code:`mritopng` in your own project ::

    import mritopng
    
    # Convert a since file
    mritopng.convert_file('/home/user/DICOM/SCAN1', '/home/user/output.png')
    
    # Convert a whole folder recursively
    mritopng.convert_folder('/home/user/DICOM/', '/home/user/PNG/')

Installation
------------

To have known to work dependencies use beforehand::

    pip install -r requirements.txt

:code:`mritopng` comes with a :code:`setup.py` script to use with distutils. After unpacking the distribution, `cd` into the
directory and execute the command::

    python setup.py install


This will install two things

 * The :code:`mritopng` module will be installed; :code:`import mritopng` will allow you to use it
 * A command line utility called :code:`mritopng` which can be used from the console

.. |Build Status| image:: https://circleci.com/gh/danishm/mritopng.svg?style=shield&circle-token=:circle-token=fdde06fc18401432d1cd84538a88678dd81584ad
.. |License| image:: https://img.shields.io/badge/License-MIT-yellow.svg
.. _License: https://opensource.org/licenses/MIT`