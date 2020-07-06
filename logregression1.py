# -*- coding: utf-8 -*-
"""
This file implements the logistic regression algorithm
with the first dataset

"""

import numpy as np
import csv
import math



def getMatrix():
    totalResults =[]
    trainInputFeatures =[]
    trainResults =[]
    testInputFeatures =[]
    testResults=[]
    inputFeatures = []
    trainMax =409
    features = ['p1_pts','p1_reb','p1_ast',
                'p2_pts','p2_reb','p2_ast',
                'p3_pts','p3_reb','p3_ast',
                'p4_pts','p4_reb','p4_ast',
                'p5_pts','p5_reb','p5_ast',
                'p6_pts','p6_reb','p6_ast',
                'op1_pts','op1_reb','op1_ast',
                'op2_pts','op2_reb','op2_ast',
                'op3_pts','op3_reb','op3_ast',
                'op4_pts','op4_reb','op4_ast',
                'op5_pts','op5_reb','op5_ast',
                'op6_pts','op6_reb','op6_ast']                
    temp =[]    
    matrices =[]
    
    with open('semifinaldataset.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        #get all input features in large list inputFeatures
        for line in csv_reader:
            if line['result']== 'W':
                totalResults.append(1)
                for feature in features:
                     temp.append(float(line[feature]))
                inputFeatures.append(temp)
                temp =[]
            else:
                totalResults.append(0)
                for feature in features:
                     temp.append(float(line[feature]))
                inputFeatures.append(temp)
                temp =[]
           
        
                
    for feature in inputFeatures[::-1]:
        if trainMax > 0:
            trainInputFeatures.append(feature)
            trainMax-=1
    
    trainMax =409
                  
        
    for result in totalResults[::-1]:
        if trainMax > 0:
            trainResults.append(result)
            trainMax -= 1
    
    
    count =0
    for result in totalResults[::-1]:
        if count > 408:
            testResults.append(result)
        count+=1
        
    count =0
    for feature in inputFeatures[::-1]:
        if count > 408:
            testInputFeatures.append(feature)
        count+=1
   
    
    trainRAInputFeatures = np.array(rollingAverages(trainInputFeatures), dtype=np.float16)
    matrices.append(trainRAInputFeatures)
    #trainNRAInputFeatures = np.array(trainInputFeatures)
    #matrices.append(trainNRAInputFeatures)
    
    resultsVector = np.array(trainResults, dtype=np.float16)
    matrices.append(resultsVector)
    
    testRAInputFeatures = np.array(rollingAverages(testInputFeatures), dtype =np.float16)
    matrices.append(testRAInputFeatures)
    
    testResultsVector = np.array(testResults,dtype=np.float16)
    matrices.append(testResultsVector)
    
    
    
    return matrices
    
    
def rollingAverages(features):
    
    RAList = []
    
    last = features[0]
    RAList.append(last)
    temp =[]
    tempTotal =[]
    for i in range(1,len(features)):
        for j in range(len(features[i])):
            total = features[i][j]+last[j]
            tempTotal.append(total)
            average =total /(i+1)
            temp.append((average))
        last = tempTotal
        tempTotal =[]
        RAList.append(temp)
        
        temp =[]
    
    return RAList
    
    
def sigmoid(x):
    answer =1/(1+ np.exp(-1*x))
    #print(answer)
    return answer

def hypothesis(X, Theta):
    return sigmoid(np.dot(Theta.transpose(),X))


def gradientDescent(Theta, X, Y, alpha):
    print(costFn(Theta,X,Y))
    for m in range(10000):
        A = hypothesis(X,Theta)
        dif = np.subtract(A,Y)
        dTheta = np.dot(X, dif)
        Theta = Theta - (alpha/409)*dTheta
        
        
    return Theta
    
        
        
    
def costFn(Theta,X,Y):
    cost = (1/409)*(-1*np.dot(Y,np.log10(hypothesis(X,Theta))) - np.dot((1-Y),np.log10(1-hypothesis(X,Theta))))
    return cost
    


def testTheta(Theta,testX,testY):
    print('new cost for test set: ')
    print(costFn(Theta,testX,testY))
    guesses = hypothesis(testX,Theta)
    print(guesses)
    tright=0
    twrong=0
    
    for i in range(223):
        if guesses[i] <= .33:
            guesses[i] =0
        if guesses[i]>.33:
            guesses[i] =1
            
    for i in range(223):
        if guesses[i] == testY[i]:
            tright+=1
        else:
            twrong +=1
    
    wCount=0
    for i in range(223):
        if testY[i]==1:
            wCount +=1
    print('win/loss pct: '+ str(wCount/223))
            
    print(testY)
    print(guesses)
    percRight  = tright/(tright+twrong)
    print('percentage of right guesses: ', percRight)
            
    
    

    
def mainAlgorithm(): 
    ms = getMatrix()
    #this X holds all training exmaples in 410x36 matrix
    Theta = np.zeros(37,)
    tX = ms[0].transpose()
    x0 = np.ones(409,)
    X = np.insert(tX, 0, x0,0)
    Y = ms[1]
    
    tx0 = np.ones(223,)
    testX = np.insert(ms[2].transpose(),0,tx0,0)
    testY = ms[3]
    alpha = .001
    costFn(Theta,X,Y)
    newTheta = gradientDescent(Theta,X,Y,alpha)

    testTheta(newTheta, testX,testY )
    

mainAlgorithm()
    
    
    