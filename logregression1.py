# -*- coding: utf-8 -*-
"""
This file implements the logistic regression algorithm
with the first dataset

"""

import numpy as np
import csv

""" getMatrix gathers the data from the csv fill and returns 
    a list with the appropiate train dataset and test dataset.
    
"""

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
    
    with open('Datasets/semifinaldataset.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # get all input features and results in large lists to then
        # be used to make numpy arrays
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
           
        
    # gathers train dataset features            
    for feature in inputFeatures[::-1]:
        if trainMax > 0:
            trainInputFeatures.append(feature)
            trainMax-=1
    
    trainMax =409
                  
    # gathers train dataset results
    for result in totalResults[::-1]:
        if trainMax > 0:
            trainResults.append(result)
            trainMax -= 1
    
    # gathers test dataset results
    count =0
    for result in totalResults[::-1]:
        if count > 408:
            testResults.append(result)
        count+=1
        
        
    # gathers test dataset features   
    count =0
    for feature in inputFeatures[::-1]:
        if count > 408:
            testInputFeatures.append(feature)
        count+=1
   
    
    #trainRAInputFeatures = np.array(rollingAverages(trainInputFeatures), dtype=np.float16)
    #matrices.append(trainRAInputFeatures)
    
    trainNRAInputFeatures = np.array(trainInputFeatures)
    matrices.append(trainNRAInputFeatures)
    
    resultsVector = np.array(trainResults, dtype=np.float16)
    matrices.append(resultsVector)
    
    testRAInputFeatures = np.array(rollingAverages(testInputFeatures), dtype =np.float16)
    matrices.append(testRAInputFeatures)
    
    #testNRAInputFeatures = np.array(testInputFeatures)
    #matrices.append(testNRAInputFeatures)
    
    
    testResultsVector = np.array(testResults,dtype=np.float16)
    matrices.append(testResultsVector)
    
    
    
    return matrices
    
""" Rolling averages function takes in game data for a certain period, 
    converts all the values so that they instead become the average value
    of that position up till that game, hence the 'rolling averages' name
    
    This is one of the ways I tested my test dataset.
    This is because the algorithm might simply learn to add up all the scores
    and when given new data about an individual game, then it will just add all
    scores values and that be the prediction.
    
    I learned that using rolling averages that this can be used to generally get 
    a sense of how a team does over time. With the lakers, we can see that generally 
    they havent won much (as the guesses are pretty low), but with generally keep 
    increasing per game (as the lakers have improved)
    

"""


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
    
    

""" Sigmoid function used to bring value of hypothesis to be between
    0 and 1. sigmoid(x) = 1/(1+e^-x)
"""
def sigmoid(x):
    answer =1/(1+ np.exp(-1*x))
    return answer


""" Hypothesis function to calculate the expected values
    given the current thetas and training examples. 
"""
def hypothesis(X, Theta):
    print(sigmoid(np.dot(Theta.transpose(),X)))
    return sigmoid(np.dot(Theta.transpose(),X))



""" Gradient descent algorithm for updating theta by 
    taking derivative of the cost function, and using it
    to change theta to minimize the cost function. 

"""

def gradientDescent(Theta, X, Y, alpha):
    
    for m in range(10000):
        A = hypothesis(X,Theta)
        dif = np.subtract(A,Y)
        dTheta = np.dot(X, dif)
        Theta = Theta - (alpha/409)*dTheta
        
    print(hypothesis(X,Theta))   
    return Theta
    
        
        


""" cost function (j(theta)) whihch is
    which uses hypothesis and current theta to tell us the given cost
"""
def costFn(Theta,X,Y):
    print(hypothesis(X,Theta))
    cost = (1/409)*(-1*np.dot(Y,np.log10(hypothesis(X,Theta))) - np.dot((1-Y),np.log10(1-hypothesis(X,Theta))))
    return cost
    


""" function tests accuracy of logistic regression algorithm results
    and tells us accuracy.
"""
def testTheta(Theta,testX,testY):
    guesses = hypothesis(testX,Theta)
    #print(guesses)
    tright=0
    twrong=0
    
    for i in range(223):
        if guesses[i] <= .5:
            guesses[i] =0
        if guesses[i]> .5:
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
    #print(testY)
    #print(guesses)
    percRight  = tright/(tright+twrong)
    print('percentage of right guesses: ', percRight)
            
    
    

""" Main function that gathers the right data and executes log regression"""
def mainAlgorithm(): 
    #calls getMatrix to get the train data/results and test data/results
    ms = getMatrix()
    #this X holds all training exmaples in 410x36 matrix
    Theta = np.zeros(37,)
    #create thetas for all features
    tX = ms[0].transpose()
    #add x0 =1 for all rows 
    x0 = np.ones(409,)
    X = np.insert(tX, 0, x0,0)
    #grab train results
    Y = ms[1]
    
    tx0 = np.ones(223,)
    testX = np.insert(ms[2].transpose(),0,tx0,0)
    testY = ms[3]
    alpha = .001
    costFn(Theta,X,Y)
    newTheta = gradientDescent(Theta,X,Y,alpha)

    #testTheta(newTheta, testX,testY )
    

mainAlgorithm()
    
    
    