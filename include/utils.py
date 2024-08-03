import matplotlib.pyplot as plt
import json
import re

from wordcloud import WordCloud as WC

def read_stop_words(lang: str, extra: list[str]):
    words = []
    with open(f'./include/nltk_data/corpora/stopwords/{lang}', 'r') as input:
        words = set([word for word in input.read().split('\n')] + extra)

    return words

def read_json(path: str) -> dict:
    """
    Wrapper function that reads a json file and returns its data.

    Args:
        path: The path to a valid json file.

    Returns:
        A json's equivalent dictionary with all its content.
    """
    data = {}

    with open(path, "r") as input_file:
        data = json.loads(input_file.read())

    return data

def print_dict(tree: dict, depth: int = 0) -> None:
    """
    Wrapper function that reads a json file and returns its data.

    Args:
        path: The path to a valid json file.

    Returns:
        A json's equivalent dictionary with all its content.
    """
    if(isinstance(tree, dict)):
        for key, val in tree.items():
            is_dict = isinstance(val, dict)
            is_list = isinstance(val, list)

            is_primitive = not is_dict and not is_list
            val_print = " " + str(val) if is_primitive else ""

            print(f'{"  " * depth}+ "{key}":{val_print}')
            print_dict(val, depth)
    elif(isinstance(tree, list)): print_list(tree, depth)

def print_list(items: list, depth: int = 0) -> None:
    """
    Wrapper function that reads a json file and returns its data.

    Args:
        path: The path to a valid json file.

    Returns:
        A json's equivalent dictionary with all its content.
    """
    for item in items:
        if(isinstance(item, list)): print_list(item, depth + 1)
        elif(isinstance(item, dict)): print_dict(item, depth + 1)
        else:
            print(f'{"  " * depth}+ {item}')

def get_vocabulary(messages: list):
    """
    Wrapper function that reads a json file and returns its data.

    Args:
        path: The path to a valid json file.

    Returns:
        A json's equivalent dictionary with all its content.
    """
    out = []
    for msg in messages: out.extend(msg.split(" "))

    return { word: 0 for word in out }

def no_accents(text: str):
    text.replace('á', 'a')
    text.replace('é', 'e')
    text.replace('í', 'i')
    text.replace('ó', 'o')
    text.replace('ú', 'u')

    return text

def clean_text(text: str, stop_words: set):
    text = no_accents(text.lower())
    tokens = re.findall(r'\w+', text)

    tokens = [
                token for token in tokens
                if token.isalpha() and token not in stop_words
                and (len(token) > 2 and len(token) < 20)
            ]

    return tokens

def get_messages_by_user(messages: list, stop_words: set):
    usr_msgs = {}

    for message in messages:
        if(not(message["type"] == "message")): continue

        msg_from = message["from"]
        usr_msgs[msg_from] = usr_msgs.get(msg_from, {
            "messages": [],
            "vocabulary": {}
        })

        text_entities = message["text_entities"]
        for entity in text_entities:
            text = entity["text"]
            usr_msgs[msg_from]["messages"].append(text)

            tokens = clean_text(text, stop_words)

            for word in tokens:
                usr_msgs[msg_from]["vocabulary"][word] = \
                    usr_msgs[msg_from]["vocabulary"].get(word, 0) + 1

    return usr_msgs

def get_global_vocabulary(user_dict: dict) -> dict:
    vocabulary = {}
    for _, d in user_dict.items():
        for word, freq in d["vocabulary"].items():
            vocabulary[word] = vocabulary.get(word, 0) + freq

    return vocabulary

def get_top_words(vocabulary: dict, top_n: int = None) -> dict:
    if(not top_n): top_n = len(vocabulary)

    return dict(sorted(
        list(vocabulary.items())[:top_n],
        key = lambda x: x[1],
        reverse = True
    ))

def create_word_cloud(freqs_dict: dict, out_path: str)  -> None:
    wc = WC(
        background_color = 'white',
        width = 1200,
        height = 1000,
        relative_scaling = 1
    )

    wc.generate_from_frequencies(freqs_dict)
    wc.to_file(out_path)

    return
