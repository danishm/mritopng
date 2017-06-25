""" A module to define the `mritopng` command line executable which is
to be included in the `scripts` folder of the python install
"""
import argparse

from . import convert_folder, convert_file


def main():
    parser = argparse.ArgumentParser(description="Convert a dicom MRI file to png")
    parser.add_argument('-f', action='store_true')
    parser.add_argument('dicom_path', help='Full path to the mri file')
    parser.add_argument('png_path', help='Full path to the generated png file')

    args = parser.parse_args()
    if args.f:
        convert_folder(args.dicom_path, args.png_path)
    else:
        convert_file(args.dicom_path, args.png_path)

if __name__ == '__main__':
    main()
