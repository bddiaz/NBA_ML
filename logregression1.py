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
    inputFeatures = []
    trainMax =410
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
        #print(inputFeatures[0])
           
        
                
    for feature in inputFeatures[::-1]:
        if trainMax > 0:
            trainInputFeatures.append(feature)
            trainMax-=1
    
    trainMax =410
            
            
            
            
            
        
    for result in totalResults[::-1]:
        if trainMax > 0:
            trainResults.append(result)
            trainMax -= 1
    trainRAInputFeatures = np.array(rollingAverages(trainInputFeatures), dtype=np.float16)
    
    matrices.append(trainRAInputFeatures)
    resultsVector = np.array(trainResults, dtype=np.float16)
    matrices.append(resultsVector)
    
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
    
    return sigmoid(np.dot(X.transpose(),Theta))


def gradientDescent(Theta, X, Y, alpha):
    for m in range(100):
        #print((np.subtract(hypothesis(X,Theta),Y)).shape)
        Theta = Theta - (alpha/410)*(np.dot(X,np.subtract(hypothesis(X,Theta),Y)))
        #print('cost after iteration: ', m)
        costFn(Theta,X,Y)
    
        
        
    
def costFn(Theta,X,Y):
    
    print((np.dot(-1*Y,np.log10(hypothesis(X,Theta)))).shape)
    
    cost = np.dot(-1*Y,np.log10(hypothesis(X,Theta))) - np.dot((1-Y),np.log10(1-hypothesis(X,Theta)))
    cost = (1/410)*cost
    
    return cost
    
        
    
    
        

    
def mainAlgorithm(): 
    ms = getMatrix()
    #this X holds all training exmaples in 410x36 matrix
    Theta = np.zeros(37,)
    tX = ms[0].transpose()
    x0 = np.ones(410,)
    X = np.insert(tX, 0, x0,0)
    
    
    Y = ms[1]
    alpha = .1
    #costFn(Theta,X,Y)
    gradientDescent(Theta,X,Y,alpha)
    
    

mainAlgorithm()
    
    
    