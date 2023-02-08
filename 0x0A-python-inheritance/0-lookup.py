#!/bin/usr/python3

def lookup(obj):
    """
    Function that returns list of available attributes
    and methods of object

    Args: 
        obj: instance of class
        
    Returns:
        Lust of attributes

    """
    return dir(obj)
