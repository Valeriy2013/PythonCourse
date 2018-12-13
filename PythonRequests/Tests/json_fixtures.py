import json
import os.path


def get_json_data(file):
    path = get_full_path(file)
    with open(path) as json_file:
        json_data = json.load(json_file)
        return json_data


def get_full_path(file):
    my_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(my_path, "../PythonRequests/DataProvider/" + file)
