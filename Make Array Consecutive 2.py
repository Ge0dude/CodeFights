# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 13:18:50 2016

@author: brendontucker
"""

def makeArrayConsecutive2(sequence):
    sequence = sorted(sequence)
    length = len(sequence)
    difference = sequence[-1] - sequence[0]
    ans = (difference - length) + 1
    return ans

