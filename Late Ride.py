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
    int2 = hourPosStr[1]
    int3 = minPosStr[0]
    int4 = minPosStr[1]
    answer = int(int1) + int(int2) + int(int3) + int(int4)
    return answer 
    
print( lateRide(n))

#works here but not in Codefights...hmmm