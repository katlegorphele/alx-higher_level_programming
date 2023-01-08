#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)

    l_len = len(my_list)

    if idx >l_len - 1:
        return (my_list)

    my_list[idx] = element

    return (my_list)
