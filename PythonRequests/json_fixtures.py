import json


def get_json_data(path):
    with open(path) as json_file:
        json_data = json.load(json_file)
        return json_data
