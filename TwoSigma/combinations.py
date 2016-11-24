# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:02:54 2016

@author: brendontucker
"""

import itertools

stocks = [[-1,2], [10,15], [11,13], [9,10]]
length = len(stocks)
iterable = range(4)
r = length 

x = 0
group = list()

while r > 0:
    list1 = list(itertools.combinations(stocks, r))
    group.append(list1)
    r = r - 1
    


