# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:14:21 2016

@author: brendontucker
"""

commands = 'AAAAA'

currPos = 0
poslist = list()
commandList = list(commands)
length1 = len(commandList)
posInList = 0
posCounter = commandList[posInList]
while posInList <= length1 - 1:
    if posCounter == 'A':
        poslist.insert(len(poslist), 0)
        currPos = 0
        posInList = posInList + 1
    if posCounter == 'L' and currPos == 0:
        poslist.insert(len(poslist), 3)
        currPos = 3
        posInList = posInList + 1
        
    