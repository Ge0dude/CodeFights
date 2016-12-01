# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:30:27 2016

@author: brendontucker
"""


false = 0
true = 1

roadRegister = [[false, true,  false, false],
                [false, false, true,  false],
                [true,  false, false, true ],
                [false, false, true,  false]]

list1 = list()                

rowNum = 0
colNum = 0
#knowlege from two sigma should help me be able to do this now--better 
#understanding of loops
while rowNum < len(roadRegister):
    if roadRegister[0][0] == 1: 
        list.append(1) #special case of top corner spot 
    elif roadRegister[rowNum][colNum] == 1:
        rowNum = colNum
        while rowNum < len(roadRegister):
            if roadRegister[rowNum][colNum] == 1:
                list1.append(1)
                break
            else:
                colNum = colNum + 1
    else:
        colNum = colNum + 1
    if colNum == len(roadRegister):
        rowNum = rowNum + 1
    
#might need to do some conditional resetting for counting ot be proper 
#on 
















'''
while rowNum < len(roadRegister):
    if roadRegister[rowNum][colNum] == 1:
        rowNum = rowNum + 1
        while rowNum < len(roadRegister):
            if roadRegister[rowNum][colNum] == 1:
                list1.append(1)
            else: 
                rowNum = rowNum + 1 
                
    else: 
        colNum = colNum + 1
'''


