#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    start = len(my_list) - 1
    for i in range(start, -1, -1):
        print("{:d}".format(my_list[i]))
