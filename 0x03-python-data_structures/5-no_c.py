#!/usr/bin/phython3
def no_c(my_string):
    remove = "c" and "C"
    new_string = ''.join(x for x in my_string if x not in remove)
    return(new_string)
