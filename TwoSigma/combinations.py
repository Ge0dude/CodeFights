# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:02:54 2016

@author: brendontucker
"""
riskBudget = 30

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


group = list()

while r > 0:
    list1 = list(itertools.combinations(stocks, r))
    group.append(list1)
    r = r - 1

valuesSum = 0

while lengthL < len(group):
    for x in group[lengthL][optionL]:
        stockValue = group[lengthL][optionL][tradeL][0]
        valuesSum = valuesSum + stockValue
        tradeL = tradeL + 1
        if tradeL == len(group[lengthL][optionL]):
            valuesList.append(valuesSum)
            valuesSum = 0
    if len(group[lengthL]) == 1:
        lengthL = lengthL + 1
        optionL = 0
        tradeL = 0
    elif optionL < (len(group[lengthL]) -1):
        optionL = optionL + 1
        tradeL = 0
    else:
        lengthL = lengthL + 1
        optionL = 0
        tradeL = 0

lengthL = 0
optionL = 0
tradeL = 0
binaryL = 0
riskSum = 0

while lengthL < len(group):
    for x in group[lengthL][optionL]:
        riskValue = group[lengthL][optionL][tradeL][1]
        riskSum = riskSum + riskValue
        tradeL = tradeL + 1
        if tradeL == len(group[lengthL][optionL]):
            riskList.append(riskSum)
            riskSum = 0
    if len(group[lengthL]) == 1:
        lengthL = lengthL + 1
        optionL = 0
        tradeL = 0
    elif optionL < (len(group[lengthL]) -1):
        optionL = optionL + 1
        tradeL = 0
    else:
        lengthL = lengthL + 1
        optionL = 0
        tradeL = 0

totalStockOptions = list(zip(valuesList, riskList))

riskValue2 = 1
stockValue2 = 0

for x in totalStockOptions:
    if totalStockOptions[stockValue2][riskValue2] > riskBudget:
        totalStockOptions.remove(totalStockOptions[stockValue2])
    stockValue2 = stockValue2 + 1

maxReturn = max(totalStockOptions)



        



