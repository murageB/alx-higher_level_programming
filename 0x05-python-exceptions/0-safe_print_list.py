#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        result = ''
        for elements in range(x):
            result += str(my_list[elements])
            counter+=1
        print('{}'.format(result))
        return counter
    except IndexError:
        counter = 0
        result = ''
        for elements in my_list:
            result += str(elements)
            counter += 1
        print('{}'.format(result))
        return counter
        
