import json

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

def print_dict(tree, depth: int = 0) -> None:
    for key, val in sorted(tree.items(), key = lambda x: x[0]):
        if(isinstance(val, dict)):
            print(f'{"  " * depth}+ "{key}":')
            print_dict(val, depth + 1)
        else:
            print(f'{"  " * depth}+ "{key}": {val}')
