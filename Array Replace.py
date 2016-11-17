# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:14:00 2016

@author: brendontucker
"""

inputArray = [1, 2, 1]
elemToReplace = 1
substitutionElem = 3

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    iterate = 0
    posInArray = inputArray[iterate]
    outputArray = list()
    while iterate < len(inputArray):
        if inputArray[iterate] == elemToReplace:
            outputArray.append(substitutionElem)
            iterate = iterate + 1
        else:
            outputArray.append(inputArray[iterate])
            iterate = iterate + 1
    return outputArray
