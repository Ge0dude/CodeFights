# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 09:17:44 2016

@author: brendontucker
"""

def isInfiniteProcess(a, b):
    
    sub = b - a 
    
    if (a and b != 0):
        if a > b:
            return True
        if b % a == 0:
            return False
        else:
            return True
    if b == 1 and (sub % 2 == 0):
        return False
    else: 
        if sub == 1:
            return True
        if sub == 2:
            return False
        if sub % 2 == 0:
            return False
        else:
            return True 
        if a > b: 
            return True