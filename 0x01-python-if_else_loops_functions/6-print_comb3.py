#!/usr/bin/python3

#Print all possible different combinations 
#of 2 numbers (Base 10)

for i in range(0,100):
    if i % 10 > i / 10:
        if i != 89:
            print("{:02d}".format(i), end=', ')
        else:
            print("{:02d}".format(i))
