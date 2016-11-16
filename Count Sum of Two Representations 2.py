# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:47:41 2016

@author: brendontucker
"""

def countSumOfTwoRepresentations2(n, l, r):
    add = l + r 
    sub = n - r 
    sub2 = r - sub
    div1 = sub2 // 2 + 1
    if l == r and add == n:
        return 1
    else:
        if n - l == 0:
            return 0
        if n - l == 1: 
            return 0
        if n - l == 2:
            return 1
        if n - l == 3:
            return 2
        else:
            return div1

