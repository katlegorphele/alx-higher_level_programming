#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0:
        return (None)

    str_len = len(my_list)

    if idx > str_len - 1:
        return (None)

    return (my_list[idx])
