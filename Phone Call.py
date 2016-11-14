# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:13:30 2016

@author: brendontucker
"""


min1 = 1
min2_10 = 2
min11 = 1
s = 6



min1Rate = int(min1)
min2Rate = int(min2_10)
min11Rate = int(min11)

counter = 0

if s > 0:
    s = s - min1Rate
    counter = 1
while s >= min2Rate and counter <= 9:
    s = s - min2Rate
    counter = counter + 1
while s >= min11Rate and counter >= 10:
    s = s - min11Rate
    counter = counter + 1
