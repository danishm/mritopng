MRI To PNG (mritopng)
=====================

A simple python module to make it easy to batch convert a binary MRI file to a PNG image.

The MRI shops hand you a CD containing your MRI scans. This CD will typically not contain
any image files that can be opened up by your defaul image viewing program. The files that
are on the CD can only be viewed using the software on the CD only on a Windows machine.

This module should help you convert all the scans to PNG files.

Important
---------

The software shows you additional meta data about the patient and the
positioning of the scan on top the scanned image. This *will not* display that information
on the PNG file.