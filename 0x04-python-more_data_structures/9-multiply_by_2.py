#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = []
    for x in range(len(a_dictionary)):
        new_dict.append(list(map((lambda x: x * 2), a_dictionary)))
    return(new_dict)
