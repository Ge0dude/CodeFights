# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 12:05:22 2016

@author: brendontucker
"""

def removeArrayPart(inputArray, l, r):
    part1 = inputArray[:l]
    part2 = inputArray[(r + 1):]
    combine = part1 + part2
    return combine 
    
#I believe directions aren't worded well?