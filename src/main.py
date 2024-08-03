import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from include.utils import *
import json

if __name__ == "__main__":
    chat = read_json("./data/in/chambaless_result.json")
    chat_name = no_accents(chat["name"].lower().replace(" ", "-"))
    stop_words = read_stop_words("spanish")

    member_messages = get_messages_by_user(chat["messages"], stop_words)

    with open(f'./data/out/{chat_name.lower()}_data.json', "w") as out:
        out.write(json.dumps(member_messages, indent = 2, ensure_ascii = False))

