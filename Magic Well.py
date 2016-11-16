# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:45:43 2016

@author: brendontucker
"""

def magicalWell(a, b, n):
    thisRoundMoney = 0
    totalMoney = 0
    while n > 0:
        thisRoundMoney = a*b 
        totalMoney = totalMoney + thisRoundMoney 
        a = a + 1
        b = b + 1
        n = n - 1
    return totalMoney
        