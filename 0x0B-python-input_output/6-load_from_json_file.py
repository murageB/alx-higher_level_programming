#!/usr/bin/python3
"""
Load from json file module

"""
import json


def load_from_json_file(filename):
    """
    creates an python object from json file

    """
    with open(filename) as f:
        return json.load(f)
