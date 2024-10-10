#!/usr/bin/env python3
from typing import List

'''
Write a type-annotated function sum_list which takes a list of floats
as argument and returns their sum as a float.
'''

def sum_list(input_list: List[float]) -> float:
    '''Return the sum of the list of floats as a float'''
    return sum(input_list)
