`mritopng` - Convert DICOM Files to PNG
=======================================

|Build Status| |License|

A simple python module to make it easy to batch convert a binary DICOM file, which is usually an output from
an MRI scan to a PNG image.

The MRI scanning facilities hand you a CD containing your MRI scans. This CD will typically not contain
any image files that can be opened up by your default image viewing program. The CD contains a list of DICOM files,
which can only be viewed by the included viewer, which is mostly only supported on a Windows machine.

This module should help you convert all the DICOM based scans to PNG files.

Important
---------

The software shows you additional meta data about the patient and the
positioning of the scan on top the scanned image. This *will not* display that information
on the PNG file.

.. |Build Status| image:: https://circleci.com/gh/danishm/mritopng.svg?style=shield&circle-token=:circle-token=fdde06fc18401432d1cd84538a88678dd81584ad
.. |License| image:: https://img.shields.io/badge/License-MIT-yellow.svg