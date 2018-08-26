""" A module to define the `mritopng` command line executable which is
to be included in the `scripts` folder of the python install
"""
import argparse

from . import convert_folder, convert_file


def main():
    parser = argparse.ArgumentParser(description="Convert a dicom MRI file to png. To conver a whole folder recursivly, use the -f option")
    parser.add_argument('-f', '--folder', action='store_true', help='Convert a whole folder instead of a single file')
    parser.add_argument('-c', '--auto-contrast', help='Apply contrast after converting default image', action="store_true")
    parser.add_argument('dicom_path', help='Full path to the mri file')
    parser.add_argument('png_path', help='Full path to the generated png file')

    args = parser.parse_args()
    print('Arguments: %s', args)
    if args.folder:
        convert_folder(args.dicom_path, args.png_path, args.auto_contrast)
    else:
        convert_file(args.dicom_path, args.png_path, args.auto_contrast)

if __name__ == '__main__':
    main()
