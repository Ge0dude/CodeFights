# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:08:21 2016

@author: brendontucker
"""

def leastFactorial(n):
    if n == 1:
        return 1
    if n <= 2:
        return 2
    if n <= 6:
        return 6
    if n <= 24:
        return 24
    else:
        return 120
    
