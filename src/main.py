import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from include.utils import *

if __name__ == "__main__":
    chat = read_json("./data/in/chambaless_result.json")
    stop_words = read_stop_words("spanish")

    member_messages = get_messages_by_user(chat["messages"])

    for member, data in member_messages.items():
        print(f'{member}:')
        data["vocabulary"] = get_vocabulary(data["messages"])

