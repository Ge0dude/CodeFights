#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 09:56:07 2017

@author: brendontucker

everything here looks 1-based instead of 0

nice! passes first two tests! 

all of the native variables have horrible names--I really 
ought to just immediatlely rename them
"""
testAnswer =[[[23,37]], 
             [[23,37]], 
             [[23,37],[1,23],[7,20],[18,18]], 
             [[18,6],[239,1]], 
             [[1,23],[7,20],[18,18]], 
             [[18,6],[239,1]], 
             [[18,6],[239,1]], 
             [[1,23],[7,20],[18,18]]]

##think tagged questions for topicIds
topicIds = [[555,666,777], 
         [8,1,239], 
         [239,566,1000]]
answerIds = [[1,2,3], 
         [239,567], 
         [566,30,8]]
views = [[1,18,5], 
         [239,23,37], 
         [567,23,0], 
         [566,1,23], 
         [30,18,18], 
         [8,7,20], 
         [3,239,1], 
         [2,18,1]]

#questionCount = len(topicIds)

uniqueTopics = []

for topics in topicIds:
    for ids in topics:
        if ids not in uniqueTopics:
            uniqueTopics.append(ids)

            
uniqueTopics.sort()

topicCount = len(uniqueTopics)   
#original code below, giong to experiment here to see if fixes
#issue with empty tagged questions
#topicCount = len(uniqueTopics)
         
topicLoc = [[] for x in range(topicCount)]

#creates a list of length equal to topicIds and anserIds that has the 
#location of each topic stored as an int, pertaining to the question
#number (0-based, so offset by one to the native counting) of its index

##basically it finds the location of the answers that pertain to teh topic
bigCounter = 0
while bigCounter < len(topicLoc):
    counter = 0
    while counter < len(topicIds):
        counter1 = 0
        while counter1 < len(topicIds[counter]):
            if topicIds[counter][counter1] == uniqueTopics[bigCounter]:
                topicLoc[bigCounter].append(counter)
            counter1 += 1
        counter += 1
    bigCounter += 1
    
viewMapping = [[] for x in range(topicCount)]

##maps answer Ids to topic. topic is the index of the list
#eg. [[3,5], [2,7]]
#topic 1 (index 0) has answerIds 3 and 5 associated with it
#topic 2 (index1) has answerIds 2 and 7 associated with it
#it is not guaranteed that all questions have a topic associated with
##them 
bigCounter = 0
while bigCounter < len(viewMapping):
    for topics in topicLoc:
        for loc in topics: #might need a if not in below here
            for item in answerIds[loc]:
                viewMapping[bigCounter].append(item)
        bigCounter += 1

 

#should be ble to sort this so that indexing is easier
#views = sorted(views)

outList = [[] for x in range(topicCount)]
userList = [[] for x in range(topicCount)]

            
#don't need this ot solve the problem, but should help undestand
#problem
userIds = []           
for answers in views:
    #print(answers)
    if answers[1] not in userIds:
        #print(views[1])
        userIds.append(answers[1])
userIds.sort()

questionsIndex = {}
for questions in views:
    #print(views.index(questions))
    indexLoc = views.index(questions)
    #key = questions[0]
    questionsIndex[questions[0]] = indexLoc
#so now I can see all unique users            
#can I just use the variable question?            
bigCount = 0
while bigCount < len(outList):
    for question in viewMapping[bigCount]:
        if views[questionsIndex[question]][1] not in userList[bigCount]: 
            print('new User detected', views[questionsIndex[question]][1])
            userList[bigCount].append(views[questionsIndex[question]][1])
            #now I need to know the index of question
            #related to the views[0] == question
            #so I think I need a dict that maps views[0]
            #to the index loc of the answer in views
            #so for question == 8, i would need {8:6}
            userView = [views[questionsIndex[question]][1], 
                        views[questionsIndex[question]][2]]
            print(userView)
            outList[bigCount].append(userView)
        else:
            #if user was found in userlist, then find the 
            #entry that has the userId and increment it
            for pair in outList[bigCount]:
                if pair[0] == views[questionsIndex[question]][1]:
                    print('pair[0] is:', pair[0])
                    pair[1] = pair[1] + views[questionsIndex[question]][2]
                    print('view Count for user', pair[0], 'incremented')
                else:
                    continue 
    
    print('NEW TOPIC')
    bigCount += 1 
            
            
    
#now I just have to clean the output data so that the ordering is
#correct, should look into teh sort() parameters

#reverseOut = [[] for x in range(topicCount)]
#
#counter = 0              
#for userCounts in outList:
#    print('this is a userCount', userCounts)
#    for pairs in userCounts:
#        #print('this is a pair', pairs)
#        #print('pair1:', pair[1], 'pair0', pair[0])
#        reverseOut[counter].append([pairs[1], pairs[0]])
#    
#    counter += 1

#now i can sort, if still trouble, reverse sort, then reverse list later    
#found a lambda that could do the job maybe            

'''
from SO 
L.sort(key=lambda k: (k[0], -k[1]), reverse=True)
'''


for groups in outList:
    groups.sort(key=lambda k: (k[1], -k[0]), reverse=True)