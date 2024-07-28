import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import json
import unittest as ut
from include.utils import *
from contextlib import redirect_stdout as redirect_out

class TestMain(ut.TestCase):

    def setUp(self):
        self.test_dict = {
            "this": "is a test",
            "number": 1,
            "testing": None,
            "boolean": True,
            "array": [1, 2, 3],
            "dict": {
                "first_key": 1,
                "second_key": 2,
            }
        }
        self.json_path = "data/in/test.json"
        self.out_path = "data/out/out.txt"

    def test_read_json(self):
        """
        Test if the function correctly reads and outputs a json.
        """
        self._create_test_json()
        expected_output = json.dumps(self.test_dict)
        output = json.dumps(read_json(self.json_path))
        self.assertEqual(
            output,
            expected_output,
            "Something went wrong when parsing json!"
        )
        self._erase_file(self.json_path)

    def test_print_dict(self):
        """
        Test if this function recursively prints the contents of a dictionary.
        """
        expected_output = "".join([
            '+ "array": [1, 2, 3]\n',
            '+ "boolean": True\n',
            '+ "dict":\n',
            '  + "first_key": 1\n',
            '  + "second_key": 2\n'
            '+ "number": 1\n',
            '+ "testing": None\n',
            '+ "this": is a test',
        ])

        with open(self.out_path, "w") as out:
            with redirect_out(out):
                print_dict(self.test_dict)

        output = ""
        with open(self.out_path, "r") as input:
            output = input.read()[:-1]

        self.assertEqual(
            expected_output,
            output,
            "Output is not equal to the expected one"
        )

        self._erase_file(self.out_path)

    def _create_temp_file(content: str = ""):
        with open(self.out_file, "w") as output:
            output.write()

    def _create_test_json(self):
        with open(self.json_path, "w") as output:
            output.write(json.dumps(self.test_dict, indent = 2))

    def _erase_file(self, path: str):
        os.remove(path)

if __name__ == "__main__":
    ut.main()
    
