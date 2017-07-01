"""Tests for mritopng"""

import os
import uuid
import tempfile
import filecmp
import unittest
import mritopng

class TestMRIToPNG(unittest.TestCase):

    def test_no_syntax_errors(self):
        """ A dummy test to make sure the mritopng library got built """
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
