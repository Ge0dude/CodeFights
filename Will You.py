# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:09:32 2016

@author: brendontucker
"""

def willYou(young, beautiful, loved):
    if young is True and beautiful is True and loved is False :
        return True
    if young is False and loved is True :
        return True
    if beautiful is False and loved is True:
        return True
    else:
        return False
    

