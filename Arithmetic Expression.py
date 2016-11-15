# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:36:52 2016

@author: brendontucker
"""

def arithmeticExpression(A, B, C):
    if A + B == C:
        return True
    if A - B == C:
        return True
    if A * B == C:
        return True
    if A / B == C:
        return True
    else:
        return False 

