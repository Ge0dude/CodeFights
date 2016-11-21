# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:02:54 2016

@author: brendontucker
"""

import itertools

iterable = range(4)
r = 4


while r > 0:
    for x in itertools.combinations(iterable, r):
        print (x)
    r = r - 1
'''
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

'''     
