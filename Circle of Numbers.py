# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 18:43:51 2016

@author: brendontucker
"""

def circleOfNumbers(n, firstNumber):
    amountToAdd = n/2 
    modSecondNumber = firstNumber + amountToAdd
    answer = modSecondNumber % n 
    return answer