import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from include.utils import *
import json

if __name__ == "__main__":
    chat = read_json("./data/in/chambaless_result.json")
    chat_name = no_accents(chat["name"].lower().replace(" ", "-"))
    stop_words = read_stop_words("spanish", [
        "jajajajaja",
        "jajaja",
        "jaja",
        "https",
        "http",
        "com",
        "solo",
        "www"
    ])

    output_folder = f'./data/out/{chat_name}' 
    if(not os.path.isdir(output_folder)):
        out.mkdir(output_folder)

    member_messages = get_messages_by_user(chat["messages"], stop_words)
    global_vocabulary_count = get_global_vocabulary(member_messages)

    for user, data in member_messages.items():
        clean_name = no_accents(user.lower().replace(" ", "-"))
        output_name = f'{output_folder}/{clean_name}_top_words.json'

        top_words = get_top_words(data["vocabulary"])

        with open(output_name, "w") as out:
            out.write(json.dumps(top_words, indent = 2, ensure_ascii = False))

