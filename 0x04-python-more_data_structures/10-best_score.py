#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not(len(a_dictionary)):
        return
    else:
        keys = list(a_dictionary.keys())
        value = list(a_dictionary.values())
        return(keys[value.index(max(value))])
