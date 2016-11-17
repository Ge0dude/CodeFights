# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:43:33 2016

@author: brendontucker
"""

arr = [1,2,3,4,5,6,7,8,9]

def firstReverseTry(arr):
    if len(arr) == 0:
        return arr 
    if len(arr) == 1:
        return arr
    if len(arr) > 0:  
        pos0 = arr[0]
        posEnd = arr[len(arr) - 1]
        arr.pop(0)
        arr.pop()
        arr.insert(0, posEnd)
        arr.insert(len(arr), pos0)
        return arr

