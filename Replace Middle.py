# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:58:28 2016

@author: brendontucker
"""

arr = [9, 0, 15, 9]
if len(arr) == 2:
    ans = arr[0] + arr[1]
if len(arr) % 2 != 0:
    ans = arr

else:
    pos1 = (len(arr) // 2) - 1
    pos2 = len(arr) // 2
    replaceValue = arr[pos1] + arr[pos2]
    arr.pop(pos1)
    arr.insert(pos2, replaceValue)
    ans = arr
    
    