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

roadRegister =  [[false,true,true,true,true], 
                 [true,false,true,true,true], 
                 [true,true,false,true,true], 
                 [true,true,true,false,true], 
                 [true,true,true,true,false]]

length = len(roadRegister)

rowNum = 0
colNum = 0
rowCount = 0
colCount = 0

boo1 = False
r = (len(roadRegister) - 1)

while r >= 0:
    rowNum = r
    colNum = 0
    rowCount = 0
    colCount = 0
    while colNum < len(roadRegister):
        if roadRegister[rowNum][colNum] == 1:
            rowCount = rowCount + 1
            colNum = colNum + 1
        else:
            colNum = colNum + 1
    colNum = r
    rowNum = 0
    while rowNum < len(roadRegister):
        if roadRegister[rowNum][colNum] == 1:
            colCount = colCount + 1
            rowNum = rowNum + 1
        else:
            rowNum = rowNum + 1
    if r == 0:
        if rowCount == colCount:
            boo1 = True
            break
    elif rowCount == colCount:
        r = r - 1 
    else:
        break

#return boo1
    



'''
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

'''            
            


