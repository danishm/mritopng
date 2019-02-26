"""Tests for mritopng"""

import os
import sys
import uuid
import shutil
import filecmp
import tempfile
import unittest
import mritopng
import traceback
import numpy as np
from mritopng import contrast


test_out_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'build', 'test'))
shutil.rmtree(test_out_path, ignore_errors=True)
os.makedirs(test_out_path)
class TestMRIToPNG(unittest.TestCase):
    """ Basic tests for mritopng """

    def test_no_syntax_errors(self):
        """ Test whether mritopng library got built """
        if 'mri_to_png' not in dir(mritopng):
            self.fail()

    def test_convert_file(self):
        """ Tests conversion of a single DICOM file """
        curr_path = os.path.dirname(os.path.realpath(__file__))
        sample_path = os.path.join(curr_path, 'data', 'samples', 'dicom1')
        expected_path = os.path.join(curr_path, 'data', 'expected', 'dicom1.png')
        actual_path = os.path.join(test_out_path, 'dicom1.png')

        print('Actual File Path: %s' % actual_path)

        # Try the file conversion
        try:
            mritopng.convert_file(sample_path, actual_path)
        except Exception as err:
            self.fail('%s' % err)

        self.assertTrue(filecmp.cmp(actual_path, expected_path),
                        'PNG generated from dicom1 does not match the expected version')
    

    def test_convert_file_with_negative_values(self):
        """ Tests DICOM files with negative values, which are clipped to 0 """

        cases = ['000012.dcm', '000017.dcm']
        curr_path = os.path.dirname(os.path.realpath(__file__))

        for case in cases:
            
            sample_path = os.path.join(curr_path, 'data', 'samples', case)
            expected_path = os.path.join(curr_path, 'data', 'expected', case + '.png')
            actual_path = os.path.join(test_out_path, case + '.png')

            print('Actual File Path: %s' % actual_path)

            # Try the file conversion
            try:
                mritopng.convert_file(sample_path, actual_path)
            except Exception as err:
                self.fail('%s' % err)
            
            self.assertTrue(filecmp.cmp(actual_path, expected_path),
                            'PNG generated from dicom1 does not match the expected version')
    
    def test_convert_file_auto_contrast(self):
        cases = ['dicom1', '000012.dcm', '000017.dcm']
        curr_path = os.path.dirname(os.path.realpath(__file__))
        os.makedirs(os.path.join(test_out_path, 'auto-contrast'))

        for case in cases:
            
            sample_path = os.path.join(curr_path, 'data', 'samples', case)
            expected_path = os.path.join(curr_path, 'data', 'expected', 'auto-contrast', case + '.png')
            actual_path = os.path.join(test_out_path, 'auto-contrast', case + '.png')

            print('Actual File Path: %s' % actual_path)

            # Try the file conversion
            try:
                print('>>> Here')
                mritopng.convert_file(sample_path, actual_path, auto_contrast=True)
                print('<<<')
            except Exception as err:
                traceback.print_exc(file=sys.stdout)
                self.fail('%s' % err)

            self.assertTrue(filecmp.cmp(actual_path, expected_path),
                            'PNG generated from dicom1 does not match the expected version')

    
    def test_contrast_histogram(self):
        curr_path = os.path.dirname(os.path.realpath(__file__))
        sample_path = os.path.join(curr_path, 'data', 'samples', '000017.dcm')
        image = mritopng.extract_grayscale_image(sample_path)
        histogram, _ = np.histogram(image.image.ravel(), np.arange(0,256))

        for bin, shade in enumerate(histogram):
            print('%d\t%d' % (shade, histogram[bin]))
        
        a = contrast.shade_at_percentile(histogram, 0.05)
        b = contrast.shade_at_percentile(histogram, 0.95)
        print("a = %d" % a)
        print("b = %d" % b)
        # raise Exception("test failed")
    
    def test_auto_contrast(self):
        image_2d = np.array([
            [0, 0, 5, 5],
            [5, 5, 5, 5],
            [5, 10, 10, 5],
            [5, 5, 5, 1]
        ])

        image = mritopng.GrayscaleImage(image_2d, 4, 4)

        result = contrast.auto_contrast(image)

        expected = np.array([
            [0, 0, 127, 127],
            [127, 127, 127, 127],
            [127, 255, 255, 127],
            [127, 127, 127, 25]
        ])

        if not np.array_equal(result.image, expected):
            raise Exception("Expected:\n%s\n\nActual:\n%s\n"%(expected, result.image))

    def test_folder_convert(self):
        curr_path = os.path.dirname(os.path.realpath(__file__))
        mri_dir_path = os.path.join(curr_path, 'data', 'samples')
        png_dir_path = os.path.join(curr_path, 'data', 'png_dir')

        mritopng.convert_folder(mri_dir_path, png_dir_path)
        
        valid_files = {'dicom1.png', '000012.dcm.png', '000017.dcm.png'}
        converted_files = set(os.listdir(png_dir_path))

        # cleanup before assertion.
        shutil.rmtree(png_dir_path)
        self.assertEqual(valid_files, converted_files, 'Invalid dicom left a stray png file.')
