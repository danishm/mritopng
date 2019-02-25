import os
import png
import pydicom
import numpy as np
from .models import GrayscaleImage
from .contrast import auto_contrast

def mri_to_png(mri_file, png_file, do_auto_contrast=False):
    """ Function to convert from a DICOM image to png

        @param mri_file: An opened file like object to read te dicom data
        @param png_file: An opened file like object to write the png data
    """

    image_2d = extract_grayscale_image(mri_file)

    if do_auto_contrast:
        image_2d = auto_contrast(image_2d)

    # Writing the PNG file
    w = png.Writer(image_2d.width, image_2d.height, greyscale=True)
    w.write(png_file, image_2d.image)

def extract_grayscale_image(mri_file):
    # Extracting data from the mri file
    plan = pydicom.read_file(mri_file)
    shape = plan.pixel_array.shape

    #Convert to float to avoid overflow or underflow losses.
    image_2d = plan.pixel_array.astype(float)

    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
    
    #Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)

    return GrayscaleImage(image_2d_scaled, shape[1], shape[0])


def convert_file(mri_file_path, png_file_path, auto_contrast=False):
    """ Function to convert an MRI binary file to a
        PNG image file.

        @param mri_file_path: Full path to the mri file
        @param png_file_path: Fill path to the png file
    """

    # Making sure that the mri file exists
    if not os.path.exists(mri_file_path):
        raise Exception('Source file "%s" does not exists' % mri_file_path)

    # Making sure the png file does not exist
    if os.path.exists(png_file_path):
        print('Removing existing output file %s' % png_file_path)
        os.remove(png_file_path)

    mri_file = open(mri_file_path, 'rb')
    png_file = open(png_file_path, 'wb')

    mri_to_png(mri_file, png_file, auto_contrast)

    png_file.close()


def convert_folder(mri_folder, png_folder, auto_contrast=False):
    """ Convert all MRI files in a folder to png files
        in a destination folder
    """

    # Create the folder for the pnd directory structure
    os.makedirs(png_folder)

    # Recursively traverse all sub-folders in the path
    for mri_sub_folder, subdirs, files in os.walk(mri_folder):
        for mri_file in os.listdir(mri_sub_folder):
            mri_file_path = os.path.join(mri_sub_folder, mri_file)

            # Make sure path is an actual file
            if os.path.isfile(mri_file_path):

                # Replicate the original file structure
                rel_path = os.path.relpath(mri_sub_folder, mri_folder)
                png_folder_path = os.path.join(png_folder, rel_path)
                if not os.path.exists(png_folder_path):
                    os.makedirs(png_folder_path)
                png_file_path = os.path.join(png_folder_path, '%s.png' % mri_file)

                try:
                    # Convert the actual file
                    convert_file(mri_file_path, png_file_path, auto_contrast)
                    print('SUCCESS: %s --> %s' % (mri_file_path, png_file_path))
                except Exception as e:
                    print('FAIL: %s --> %s : %s' % (mri_file_path, png_file_path, e))
                    os.remove(png_file_path) if os.path.exists(png_file_path) else None
