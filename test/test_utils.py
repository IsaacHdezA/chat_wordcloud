import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import json
import unittest as ut
from include.utils import *
from contextlib import redirect_stdout as redirect_out

class TestMain(ut.TestCase):
    def setUp(self):
        self.test_msgs = {
          "name": "User 1",
          "messages": [
            {
              "from": "User 1",
              "text": "Ahora si me vas a poder carrear bien maestro",
              "text_entities": [
                {
                  "type": "plain",
                  "text": "Ahora si me vas a poder carrear bien maestro"
                }
              ]
            }
          ]
        }
        self.test_struct = {
            "User 1": {
                "messages": ["Ahora si me vas a poder carrear bien maestro"]
            }
        }

        self.json_path = "data/in/test.json"
        self.out_path = "data/out/out.txt"

    def test_read_json(self):
        """
        Test if the function correctly reads and outputs a json.
        """
        self._create_test_json(self.test_msgs)
        expected_output = json.dumps(self.test_msgs)
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
            '+ "name": User 1\n',
            '+ "messages":\n',
            '  + "from": User 1\n',
            '  + "text": Ahora si me vas a poder carrear bien maestro\n',
            '  + "text_entities":\n',
            '    + "type": plain\n',
            '    + "text": Ahora si me vas a poder carrear bien maestro'
        ])

        with open(self.out_path, "w") as out:
            with redirect_out(out):
                print_dict(self.test_msgs)

        output = ""
        with open(self.out_path, "r") as input:
            output = input.read()[:-1]

        self.assertEqual(
            expected_output,
            output,
            "Output is not equal to the expected one"
        )

        self._erase_file(self.out_path)

    def test_get_vocabulary(self):
        """
        Get full vocabulary from a user in a chat from its messges.
        """
        expected_output = {
            "Ahora", "si", "me", "vas", "a",
            "poder", "carrear", "bien", "maestro"
        }
        output = get_vocabulary(self.test_struct["User 1"]["messages"])
        self.assertEqual(
            output,
            expected_output,
            "Current vocabulary does not match with expected vocabulary"
        )

    def _create_temp_file(content: str = ""):
        with open(self.out_file, "w") as output:
            output.write()

    def _create_test_json(self, obj: dict):
        with open(self.json_path, "w") as output:
            output.write(json.dumps(obj, indent = 2))

    def _erase_file(self, path: str):
        os.remove(path)

if __name__ == "__main__":
    ut.main()
    
