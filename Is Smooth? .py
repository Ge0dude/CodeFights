# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 12:41:13 2016

@author: brendontucker
"""

boo1 = False
boo2 = False
boo3 = False


array1 = [-12, 34, 40, -5, -12, 4, 0, 0, -12]
if len(array1) % 2 == 0: #if even
    length1 = len(array1) / 2
    length2 = int(length1)
    index1 = array1[length2 - 1]
    index3 = array1[-length2]
    ans1 = (array1[length2 - 1] + array1[-length2])
    if ans1 == array1[0]:
        boo1 = True
    if ans1 == array1[-1]:
        boo2 = True
    if boo1 == True and boo2 == True:
        boo3 = True

if len(array1) % 2 != 0: #if odd
    length3 = (len(array1) // 2) 
    if array1[length3] == array1[0]:
        boo1 = True
    if array1[length3] == array1[-1]:
        boo2 = True
    if boo1 == True and boo2 == True:
        boo3 = True   
    
    
    
    
    
    

