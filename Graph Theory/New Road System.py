# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:21:07 2016

@author: brendontucker
"""
'''
could try a functional approach here, define a row searcher
and define a colum searcher, if they're both true, for all options, 
then return True

'''

false = False
true = True
'''
counter = 0
var1 = 0
boo1 = False
boo2 = False 
'''

roadRegister = [[false, true,  false, false],
                [false, false, true,  false],
                [true,  false, false, true ],
                [false, false, true,  false]]
length = len(roadRegister)

