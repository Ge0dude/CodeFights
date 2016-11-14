# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 19:00:12 2016

@author: brendontucker
"""

n = 808
def lateRide(n):
    hourPosition = n // 60
    minutePosition = n - (hourPosition * 60)
    hourPosStr = str(hourPosition)
    minPosStr = str(minutePosition)
    int1 = hourPosStr[0]
    int3 = minPosStr[0]
    if len(hourPosStr) > 1:
        int2 = int(hourPosStr[1])
    else: 
        int2 = 0
    if len(minPosStr) > 1:
        int4 = int(minPosStr[1])
    else: 
        int4 = 0
    answer = int(int1) + int(int2) + int(int3) + int(int4)
    return answer 
    
print( lateRide(n))
