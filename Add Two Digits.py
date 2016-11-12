# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 13:11:54 2016

@author: brendontucker
"""


n = 78
def addTwoDigits(n):
    nAsAString = str(n)
    int1 = nAsAString[0]
    int2 = nAsAString[1]
    int3 = int(int1) + int(int2)
    return int3
    
print (addTwoDigits(n))
