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

valuesSum = 0

for x in group:
    for x in group[lengthL][optionL]:
        stockValue = group[lengthL][optionL][tradeL][0]
        valuesSum = valuesSum + stockValue
        tradeL = tradeL + 1
        if tradeL == len(group[lengthL][optionL]):
            valuesList.append(valuesSum)
            valuesSum = 0
    if optionL < (len(group[lengthL]) -1):
        optionL = optionL + 1
        tradeL = 0
    else:
        lengthL = lengthL + 1
        optionL = 0
        tradeL = 0


'''
#I think this one is really close, just need to alter
#where the valuesSum is happening, need to go back to inner loop
while lengthL <= (len(group) - 1):
    while optionL <= (len(group[lengthL]) - 1):
        for x in group[lengthL][optionL]:
            stockValue = group[lengthL][optionL][tradeL][0]
            valuesSum = valuesSum + stockValue
            tradeL = tradeL + 1
            if tradeL == (len(group[lengthL][tradeL]) - 1):
                valuesList.append(valuesSum)
                valuesSum = 0
        optionL = optionL + 1
    lengthL = lengthL + 1
'''

'''
for x in group:
    while lengthL < len(group):
        for x in group[lengthL]:
            while optionL < len(group[lengthL]):
                for x in group[lengthL][optionL]:
                    while tradeL < len(group[lengthL][optionL]):
                        stockValue = group[lengthL][optionL][tradeL][0]
                        valuesSum = valuesSum + stockValue
                        tradeL = tradeL + 1
                valuesList.append(valuesSum)
                valuesSum = 0
                optionL = optionL + 1
            valuesList.append(valuesSum)
            valuesSum = 0
            optionL = optionL + 1   
        lengthL = lengthL + 1
'''
'''
for x in group[lengthL][optionL]:
    stockValue = group[lengthL][optionL][tradeL][0]
    valuesSum = valuesSum + stockValue
    tradeL = tradeL + 1
valuesList.append(valuesSum)
valuesSum = 0
optionL = optionL + 1
'''
'''
while optionL < len(group[lengthL]):
    while tradeL < len(group[lengthL][optionL]):
        stockValue = group[lengthL][optionL][tradeL][0]
        valuesSum = valuesSum + stockValue
        tradeL = tradeL + 1
    valuesList.append(valuesSum)
    valuesSum = 0
    optionL = optionL + 1
lengthL = lengthL + 1
'''
'''
while tradeL < len(group[lengthL][optionL]):
    stockValue = group[lengthL][optionL][tradeL][0]
    valuesSum = valuesSum + stockValue
    tradeL = tradeL + 1
valuesList.append(valuesSum)
valuesSum = 0
optionL = optionL + 1
'''
'''
while optionL < len(group[lengthL]):
lengthL = lengthL + 1
'''

'''
if optionL >= len(group[lengthL]):
    lengthL = lengthL + 1
'''
'''
while lengthL < len(group):
    while optionL < len(group[lengthL]):
        while tradeL < len(group[lengthL][optionL]):
            stockValue = group[lengthL][optionL][tradeL][0]
            valuesSum = valuesSum + stockValue
            tradeL = tradeL + 1
        valuesList.append(valuesSum)
        valuesSum = 0
        optionL = optionL + 1    
    lengthL = lengthL + 1
'''



