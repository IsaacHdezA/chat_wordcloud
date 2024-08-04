import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from sys import argv
from include.utils import *
import json

if __name__ == "__main__":
    argv = argv[1:]
    argc = len(argv)

    if(argc < 1 or argc > 1):
        print(f'Wrong usage:\npython main.py path/to/chat.json')
        exit(1)

    input_file = argv[0]

    chat = read_json(input_file)
    chat_name = no_accents(chat["name"].lower().replace(" ", "-"))
    stop_words = read_stop_words("spanish", [
        "jajajajaja",
        "jajaja",
        "jaja",
        "https",
        "http",
        "www"
        "com",
        "solo",
    ])

    print(f'Reading "{argv[0].split("/")[-1]}"...')

    output_root = './data/out'
    output_folder = f'{output_root}/{chat_name}' 
    img_folder = output_folder + '/img'

    if(not os.path.isdir('./data')):
        print(f'No data folder detected. Creating...\n')
        os.makedirs(img_folder)

    print(f'Reading messages and getting data...')
    member_messages = get_messages_by_user(chat["messages"], stop_words)
    global_vocabulary_count = get_global_vocabulary(member_messages)

    print(f'Generating Word Clouds...')
    for user, data in member_messages.items():
        clean_name = no_accents(user.lower().replace(" ", "-"))
        output_name = f'{img_folder}/{clean_name}'

        top_words = get_top_words(data["vocabulary"])

        with open(f'{output_folder}/{clean_name}_top_words.json', "w") as out:
            out.write(json.dumps(top_words, indent = 2, ensure_ascii = False))

        create_word_cloud(top_words, f'{img_folder}/{clean_name}_word_cloud.png')
        print(f'\t! "{user}" Word Cloud done.')

    create_word_cloud(global_vocabulary_count, f'{img_folder}/global_word_cloud.png')

    print(f'\nDone. You can find your data in {output_folder}')

