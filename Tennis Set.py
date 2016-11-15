# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:51:48 2016

@author: brendontucker
"""

def tennisSet(score1, score2):
    if score1 == 6 and score2 < 5:
        return True
    if score1 == 7 and score2 > 4 and score2 < 7 :
        return True 
    if score2 == 6 and score1 < 5:
        return True
    if score2 == 7 and score1 > 4 and score1 < 7:
        return True
    else:
        return False 

