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

#rowsolver
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



