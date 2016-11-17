# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:14:21 2016

@author: brendontucker
"""

'''

'A' as a first entry seems to throw somekind of 
error where all 0s are returned. Don't know why.
pos may not be the right value to replace...
'''

commands = 'ALLALLLL'

currPos = 0
poslist = list()
commandList = list(commands)
length1 = len(commandList)
posInList = 0
posCounter = commandList[posInList]
while posInList <= length1 - 1:
    if commandList[posInList] == 'A':
        poslist.insert(len(poslist), 0)
        currPos = 0
        posInList = posInList + 1
    if posCounter == 'L' and currPos == 0:
        poslist.insert(len(poslist), 3)
        currPos = 3
        posInList = posInList + 1
    if posCounter == 'L' and currPos == 1:
        poslist.insert(len(poslist), 0)
        currPos = 0
        posInList = posInList + 1
    if posCounter == 'L' and currPos == 2:
        poslist.insert(len(poslist), 1)
        currPos = 1
        posInList = posInList + 1
    if posCounter == 'L' and currPos == 3:
        poslist.insert(len(poslist), 2)
        currPos = 2
        posInList = posInList + 1
        
    