# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 11:30:27 2016

@author: brendontucker
"""

#same number of roads is what is important.. oh no!
#also need a condition for if there is no True value in a row, and if there 
#is mroe than one true value... similar logic should apply
#but creating the answer will be much more complex
#don't know what data type to use yet
false = 0
true = 1

roadRegister =  [[false,true,false,false,false,false,false], 
                 [true,false,false,false,false,false,false], 
                 [false,false,false,true,false,false,false], 
                 [false,false,true,false,false,false,false], 
                 [false,false,false,false,false,false,true], 
                 [false,false,false,false,true,false,false], 
                 [false,false,false,false,false,true,false]]

list1 = list()                

rowNum = 0
colNum = 0
#knowlege from two sigma should help me be able to do this now--better 
#understanding of loops
r = (len(roadRegister) - 1)
#something about special case if row and col num have been found needed
#in first if block
while r >= 0:
    rowNum = r
    if roadRegister[rowNum][colNum] == 1:
        colNum = rowNum
        rowNum = 0
        while rowNum <= (len(roadRegister) - 1):
            if roadRegister[rowNum][colNum] == 1:
                list1.append(1)
                r = r - 1
                colNum = 0
                break
            else:
                rowNum = rowNum + 1
    else:
        if colNum == (len(roadRegister) - 1):
            r = r - 1
        else:
            colNum = colNum + 1

if len(list1) == len(roadRegister):
    ans = True
else:
    ans = False

            
            


