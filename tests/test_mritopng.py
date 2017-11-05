"""Tests for mritopng"""

import os
import uuid
import tempfile
import filecmp
import unittest
import mritopng

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
        actual_path = os.path.join(tempfile.gettempdir(), '%s.%s' % (uuid.uuid4(), "png"))

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
            actual_path = os.path.join(tempfile.gettempdir(), '%s.%s' % (uuid.uuid4(), "png"))

            print('Actual File Path: %s' % actual_path)

            # Try the file conversion
            try:
                mritopng.convert_file(sample_path, actual_path)
            except Exception as err:
                self.fail('%s' % err)
            
            self.assertTrue(filecmp.cmp(actual_path, expected_path),
                            'PNG generated from dicom1 does not match the expected version')
