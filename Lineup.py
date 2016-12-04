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



currPos = 0

#mod function
def modCurr(currPos):
    if currPos == 4:
        currPos = 0
    if currPos == -1:
        currPos = 3
    return currPos
    
    
commands = 'RLR'
poslist = list()
length1 = len(commands)
posInList = 0

while posInList <= length1 - 1:
    if commands[posInList] == 'L':
        currPos = currPos - 1
        if currPos == 4:
            currPos = 0
        if currPos == -1:
            currPos = 3
        poslist.append(currPos)
        posInList = posInList + 1
    elif commands[posInList] == 'R':
        currPos = currPos + 1
        if currPos == 4:
            currPos = 0
        if currPos == -1:
            currPos = 3
        poslist.append(currPos)
        posInList = posInList + 1
    elif commands[posInList] == 'A':
        currPos = 0
        poslist.append(currPos)
        posInList = posInList + 1
        
poslist2 = list()
posInList = 0
currPos = 0

while posInList <= length1 - 1:
    if commands[posInList] == 'R':
        currPos = currPos - 1
        if currPos == 4:
            currPos = 0
        if currPos == -1:
            currPos = 3
        poslist2.append(currPos)
        posInList = posInList + 1
    elif commands[posInList] == 'L':
        currPos = currPos + 1
        if currPos == 4:
            currPos = 0
        if currPos == -1:
            currPos = 3
        poslist2.append(currPos)
        posInList = posInList + 1
    elif commands[posInList] == 'A':
        currPos = 0
        poslist2.append(currPos)
        posInList = posInList + 1
        
counter = 0
posInList = 0
while posInList <= length1 - 1:
    if poslist[posInList] == poslist2[posInList]:
        counter = counter + 1
        posInList = posInList + 1
    else:
        posInList = posInList + 1
        







