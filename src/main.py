import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from include.utils import *

if __name__ == "__main__":
    chat = read_json("./data/in/result.json")
    print(chat)

