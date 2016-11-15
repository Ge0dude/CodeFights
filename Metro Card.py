# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:39:32 2016

@author: brendontucker
"""

def metroCard(lastNumberOfDays):
    if lastNumberOfDays == 31:
        return [28, 30, 31]
    else:
        return [31]


