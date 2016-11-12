# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:18:41 2016

@author: brendontucker
"""

def seatsInTheater(nCols, nRows, col, row):
    answer = (nRows - row) * (nCols - (col - 1))
    return answer 
