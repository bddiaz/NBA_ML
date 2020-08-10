# -*- coding: utf-8 -*-
"""
Neural Network implementation

Here, I implemented a 4 layer neural network to make predictions on the 
probability of a home team beating the away team in nba game.

The network was trained with 6000 games starting with the 2012 season.

The network was then tested on 3509 games, up until the 2019 season
(not including the NBA bubble games from Orlando)

The accuracy achieved is around 68%!

"""
import numpy as np
import csv


""" Function returns the matrix which contains all the training examples
    and the results of those traning examples
"""
def matrices():
    trainX =[]
    with open('normalizedTrainData.csv','r') as trainFile:
        csv_reader = csv.reader(trainFile)
        
        for line in csv_reader:
            trainX.append(line)
    '''
    indices = [16,24,32,40,48,56,64,72,80,88,96,104]
    for x in trainX:
        for index  in indices[::-1]:
            del x[index]
    '''       
        
    
    trainY = []
    with open('dataResults.csv', 'r') as trainResultsFile:
        csv_reader1 = csv.reader(trainResultsFile)
        i = 0
        for line in csv_reader1:
            if i < 6000:
                trainY.append(line[0])
                i+=1
    
    #featureNormalization(trainX)
    
    
    tX = np.array(trainX, dtype = np.float64)
    Y = np.array(trainY, dtype = np.float64).reshape((1,6000))
    X = tX.transpose()
    matrixs = []
    matrixs.append(X)
    matrixs.append(Y)
    
    return matrixs
  


""" This function was used to normalize the training data so that each data point 
    was a value between 0 and 1. The method to do this was: (x-min)/(max-min)
    where x is a particular feature. This is used for both train and test data.
"""
def featureNormalization(X):
    
    for i in range(100):
        tfeature= []
        for j in range(3509):   
            tfeature.append(float(X[j][i]))
        for j in range(3509):
            X[j][i] = (float(X[j][i])-min(tfeature))/(max(tfeature)-min(tfeature))
            
    with open('normalizedTestData.csv','w') as newFile:
        csv_writer = csv.writer(newFile, lineterminator = '\n')
        
        for i in range(3509):
            csv_writer.writerow(X[i])


""" Function to retrive our test data and normalized it like we did with the 
    train data.
"""
        
def maketestData():
    testDataX =[]
    with open('TrainAndTestData/testData.csv','r') as testDataFile:
        
        csv_reader = csv.reader(testDataFile)
        
        for line in csv_reader:
            testDataX.append(line)
    
    indices = [16,24,32,40,48,56,64,72,80,88,96,104]
    for x in testDataX:
        for index  in indices[::-1]:
            del x[index]
            
    featureNormalization(testDataX)
           


""" Function to compute the RELU activation function for first 3 layers"""
def relu(Z):
    return np.maximum(0,Z)
    

""" Function to compute Sigmoid activation function for last layer """
def sigmoid(Z):
    return 1/(1 + np.exp(-1*Z))


""" Derivative of RELU activation function for backprop"""
def dRelu(Z):
    Z[Z<=0]=0
    Z[Z>0]=1
    return Z
    

""" Manually defined forward propagation function that immediately calls on 
    the backprop function in order to automatically complete one epoch. The function
    also returns the results of the backprop function (aka the derivatives of the weights and biases)
"""
def forwardProp(X,Y,m,alpha,numLayers,W0,W1,W2,W3,b0,b1,b2,b3):

    Z0 = (W0 @ X) + b0
    A1= relu(Z0)
    
    
    Z1 = (W1 @ A1) + b1
    A2 = relu(Z1)
    
    Z2 = (W2 @ A2) + b2
    A3 = relu(Z2)
    
    Z3 = (W3 @ A3) + b3
    A4 = sigmoid(Z3)
      
    return backProp(X,Y,m,alpha,numLayers,W0,W1,W2,W3,b0,b1,b2,b3,Z0,Z1,Z2,Z3,A1,A2,A3,A4)
    
    
    
""" Manually implemented backprop function used to compute the derivatives
    of our weights and biases (stored in a list of results)
"""

 
def backProp(X,Y,m,alpha,numLayers,W0,W1,W2,W3,b0,b1,b2,b3,Z0,Z1,Z2,Z3,A1,A2,A3,A4):
    
    dZ3 = A4 - Y
    dW3 = (1/m)*(np.dot(dZ3,A3.transpose()))    
    db3 = (1/m)*(np.sum(dZ3, axis =1, keepdims = True))
    
    dA2 = np.dot(W3.transpose(),dZ3)
    dZ2 = np.multiply(dA2,dRelu(Z2))
    dW2 = (1/m)*(np.dot(dZ2,A2.transpose())) 
    db2 = (1/m)*(np.sum(dZ2, axis =1, keepdims = True))
    
    dA1 = np.dot(W2.transpose(),dZ2)
    dZ1 = np.multiply(dA1,dRelu(Z1))
    dW1 = (1/m)*(np.dot(dZ1,A1.transpose())) 
    db1 = (1/m)*(np.sum(dZ1, axis =1, keepdims = True))
    
    dA0 = np.dot(W1.transpose(),dZ1)
    dZ0 = np.multiply(dA0,dRelu(Z0))
    dW0 = (1/m)*(np.dot(dZ0,X.transpose()))
    db0 = (1/m)*(np.sum(dZ0, axis =1, keepdims = True))
    
    derivs = [dW0,db0,dW1,db1,dW2,db2,dW3,db3,A4]
    return derivs
    

""" Cost function to keep track of how well our algorithm is performing"""

def cost(m,Y,A4):
    A4 = A4.transpose()
    cost = (-1/m)*(np.dot(Y,np.log(A4)) + np.dot(1-Y,np.log(1-A4)))
    return cost
   
 
""" Funciton to test our new weights and biases on data which has not been seen
    by the algorithm. This also creates a file for us to look a the reults in depth.
"""  
def testData(W0,W1,W2,W3,b0,b1,b2,b3):
    normTestData =[]
    with open('normalizedTestData.csv','r') as testfile:
        csv_reader = csv.reader(testfile)
        for line in csv_reader:
            normTestData.append(line)
    
    
    X = np.array(normTestData, dtype = np.float64)
    X = X.transpose()
    Z0 = (W0 @ X) + b0
    A1= relu(Z0)
    
    
    Z1 = (W1 @ A1) + b1
    A2 = relu(Z1)
    
    Z2 = (W2 @ A2) + b2
    A3 = relu(Z2)
    
    Z3 = (W3 @ A3) + b3
    A4 = sigmoid(Z3)
    
    testY =[]
    with open('dataResults.csv', 'r') as trainResultsFile:
        csv_reader1 = csv.reader(trainResultsFile)
        i = 0
        for line in csv_reader1:
            if i >= 6000:
                testY.append(float(line[0]))
                i+=1
            else:
                i+=1
    
    correct = 0
    predY = []
    for i in range(3509):
        if A4[0][i] > .5:
            predY.append(1)
        else:
            predY.append(0)
            
     
    rawPred =[]
    for i in range(3509):
        rawPred.append(A4[0][i])
        
    for i in range(3509):
        if predY[i] == testY[i]:
            correct+=1
    
    print(rawPred)
    print(predY)
    print('number of correct guesses: ' + str(correct))
    print('percentage of correct guesses: ' + str(correct/3509))
    

    with open('testRawPred.csv','w') as testfile:
        csv_writer = csv.writer(testfile, lineterminator = '\n')
        
        for i in range(3509):
            temp = [rawPred[i]]
            csv_writer.writerow(temp)
        
    with open('testPred.csv','w') as testfile1:
        csv_writer = csv.writer(testfile1, lineterminator = '\n')
        
        for i in range(3509):
            temp = [predY[i]]
            csv_writer.writerow(temp)
    

""" The main function to set algorithm in motion. It gets our traning examples
    and results. Then, we initialize all of our weights and biases matrices of 
    the respective sizes for each layer. Then, we use a loop to call the forwardprop
    function, which automatically calls on backprop. From this call, we get the 
    derivatives of all of the weights and biases of all the layers, and so we use these
    results to update such biases and weights. This is where our traning occurs. 
"""
  
def main():
    matrixs = matrices()
    X = matrixs[0]
    Y = matrixs[1]
    
    m = 6000
    numLayers = 4
    alpha = .01
    
    W0 = np.random.rand(30,100)
    W0 = W0/10
    b0 = np.zeros((30,1))
    
    
    W1= np.random.rand(15,30)
    W1 = W1/10
    b1= np.zeros((15,1))
    
    W2 = np.random.rand(12,15)
    W2 = W2/10
    b2 = np.zeros((12,1))
    
    W3 = np.random.rand(1,12)
    b3 = np.zeros((1,1))
    
    
    epochs = 10000
    
    for epoch in range(epochs):
        d = forwardProp(X,Y,m,alpha,numLayers,W0,W1,W2,W3,b0,b1,b2,b3)
        
        W0 = W0 - alpha*(d[0])
        b0 = b0 - alpha*(d[1])
        W1 = W1 - alpha*(d[2])
        b1 = b1 - alpha*(d[3])
        W2 = W2 - alpha*(d[4])
        b2 = b2 - alpha*(d[5])
        W3 = W3 - alpha*(d[6])
        b3 = b3 - alpha*(d[7])
        A4 = d[8]
        cost(m,Y,A4)

    testData(W0,W1,W2,W3,b0,b1,b2,b3)
 

    
    
main()

