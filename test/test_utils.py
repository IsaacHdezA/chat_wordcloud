import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import unittest as ut
from include.utils import *

class TestMain(ut.TestCase):
    def test_read_json(self):
        """
        Test if the function correctly reads and outputs a json.
        """
        self.assertEqual(read_json("ramiro"), {}) # Error or something

if __name__ == "__main__":
    ut.main()
