# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 08:26:47 2016

@author: brendontucker
"""

value1 = 10
weight1 = 5
value2 = 6
weight2 = 4
maxW = 8


def largerValue(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2

def knapsackLight(value1, weight1, value2, weight2, maxW):
    totalValue = 0

    if weight1 + weight2 <= maxW:
        totalValue = value1 + value2
    if weight1 + weight2 > maxW and weight1 <= maxW and weight2 <= maxW:
        totalValue = largerValue(value1, value2)    
    if weight1 + weight2 > maxW and weight1 > maxW and weight2 <= maxW:
        totalValue = value2
    if weight1 + weight2 > maxW and weight2 > maxW and weight1 <= maxW:    
        totalValue = value1
    if weight1 > maxW and weight2 > maxW:
        totalValue = 0
    return totalValue 

