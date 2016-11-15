# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 08:13:48 2016

@author: brendontucker
"""

def reachNextLevel(experience, threshold, reward):
    nxtLevel = False

    if experience + reward < threshold:
        nxtLevel = nxtLevel
    if experience + reward >= threshold:
        nxtLevel = True
    return nxtLevel 

