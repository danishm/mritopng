"""Tests for mritopng"""

import unittest
import mritopng

class TestMRIToPNG(unittest.TestCase):

    def test_skeleton(self):
        """ A dummy test to make sure the mritopng library got built """
        if 'mri_to_png' not in dir(mritopng):
            self.fail()
