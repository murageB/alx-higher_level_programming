#!/usr/bin/python3
"""
Object to JSON string Module

"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    """
    return json.dumps(my_obj)
