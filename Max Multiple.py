# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 18:37:27 2016

@author: brendontucker
"""

def maxMultiple(divisor, bound):
    modAnswer = bound % divisor 
    answer = bound - modAnswer 
    return answer 
        