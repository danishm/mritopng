import os
import png
import dicom
import argparse


def mri_to_png(mri_file, png_file):

    # Extracting data from the mri file
    plan = dicom.read_file(mri_file)
    shape = plan.pixel_array.shape

    image_2d = []
    max_val = 0
    for row in plan.pixel_array:
        pixels = []
        for col in row:
            pixels.append(col)
            if col > max_val: max_val = col
        image_2d.append(pixels)

    # Rescaling grey scale between 0-255
    image_2d_scaled = []
    for row in image_2d:
        row_scaled = []
        for col in row:
            col_scaled = int((float(col) / float(max_val)) * 255.0)
            row_scaled.append(col_scaled)
        image_2d_scaled.append(row_scaled)

    # Writing the PNG file
    w = png.Writer(shape[0], shape[1], greyscale=True)
    w.write(png_file, image_2d_scaled)


def convert_file(mri_file_path, png_file_path):
    """ Function to convert an MRI binary file to a
        PNG image file.

        @param mri_file_path: Full path to the mri file
        @param png_file_path: Fill path to the png file
    """

    # Making sure that the mri file exists
    if not os.path.exists(mri_file_path):
        raise Exception('File "%s" does not exists' % mri_file_path)

    # Making sure the png file does not exist
    if os.path.exists(png_file_path):
        raise Exception('File "%s" already exists' % png_file_path)

    mri_file = open(mri_file_path, 'r')
    png_file = open(png_file_path, 'wb')

    mri_to_png(mri_file, png_file)

    png_file.close()


def convert_folder(mri_folder, png_folder):
    """ Convert all MRI files in a folder to png files
        in a destinaiton folder
    """
    os.makedirs(png_folder)
    for mri_file in os.listdir(mri_folder):
        mri_file_path = os.path.join(mri_folder, mri_file)
        png_file_path = os.path.join(png_folder, '%s.png' % mri_file)
        try:
            convert_file(mri_file_path, png_file_path)
            print mri_file_path, '-->', png_file_path
        except:
            print 'FAIL>', mri_file_path, '-->', png_file_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert a dicom MRI file to png",
                                     usage='mritopng.py [path to dicom file] [path to png file]')
    parser.add_argument('mri_file', help='Full path to the mri file')
    parser.add_argument('png_file', help='Full path to the generated png file')

    args = parser.parse_args()
    convert_file(args.mri_file, args.png_file)