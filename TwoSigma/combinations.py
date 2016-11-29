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
valuesList = list()
riskList = list()
lengthL = 0
optionL = 0
tradeL = 0
binaryL = 0 

x = 0
group = list()

while r > 0:
    list1 = list(itertools.combinations(stocks, r))
    group.append(list1)
    r = r - 1


while lengthL < len(group):
    while optionL < len(group[lengthL][optionL]):
        while tradeL < len(group[lengthL][optionL][tradeL]):
            valueSum = 
            valuesList.append(group[lengthL][optionL][tradeL][0])
            tradeL = tradeL + 1
        optionL = optionL + 1
    lengthL = lengthL + 1
        
    


