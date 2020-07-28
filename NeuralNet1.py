# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:36:18 2020

@author: 17732
"""
import numpy as np
import csv

def matrices():
    trainX =[]
    with open('TrainAndTestData/trainData.csv','r') as trainFile:
        csv_reader = csv.reader(trainFile)
        
        for line in csv_reader:
            trainX.append(line)
    
    indices = [16,24,32,40,48,56,64,72,80,88,96,104]
    for x in trainX:
        for index  in indices[::-1]:
            del x[index]
            
        
    
    trainY = []
    with open('dataResults.csv', 'r') as trainResultsFile:
        csv_reader1 = csv.reader(trainResultsFile)
        i = 0
        for line in csv_reader1:
            if i < 6000:
                trainY.append(line[0])
                i+=1
    
    tX = np.array(trainX, dtype = np.float64)
    Y = np.array(trainY, dtype = np.float64)
    X = tX.transpose()
    matrixs = []
    matrixs.append(X)
    matrixs.append(Y)
    
    return matrixs
    
def initializeWeights():
    result =[]
    W1 = np.random.rand(30,100)
    W2 = np.random.rand(15,30)
    W3 = np.random.rand(12,15)
    W4 = np.random.rand(1,12)
    
    result.append(W1)
    result.append(W2)
    result.append(W3)
    result.append(W4)
    return result

def initializeBias():
    result =[]
    b1 = np.zeros((30,1))
    b2 = np.zeros((15,1))
    b3 = np.zeros((12,1))
    b4 = np.zeros((1,1))
    
    result.append(b1)
    result.append(b2)
    result.append(b3)
    result.append(b4)
    return result




def relu(Z):
    return np.maximum(0,Z)
    
    
def sigmoid(Z):
    return 1/(1 + np.exp(-1*Z))

def dRelu(Z):
    Z[Z<=0]=0
    Z[Z>0]=1
    return Z
    
def forwardProp(X,Y,m,alpha,numLayers):
    epochs = 1
    Zs =[]
    Ws = initializeWeights()
    Bs = initializeBias() 
    
    for epoch in range(epochs):
        #print(epoch)
        As = []
        As.append(X)
        for i in range(numLayers-1):
            z = (Ws[i] @ As[i]) + Bs[i]
            Zs.append(z)
            a = relu(z)
            As.append(a)

        z = (Ws[3] @ As[3]) + Bs[3]
        Zs.append(z)
        a = sigmoid(z)
        As.append(a)
        
        
        
        
        dAs =[0,0,0]
        dWs =[0,0,0,0]
        dBs =[0,0,0,0]
        
        
        dZ = As[4] - Y
 
        dW = (1/m)* np.dot(dZ, As[3].transpose())

        dB = 1/m * (np.sum(dZ,axis =1, keepdims = True))
        dWs[3] = dW
        dBs[3] = dB
        dAs[2]= np.dot(Ws[3].transpose(),dZ)
        Ws[3] = Ws[3]- (alpha*dWs[3])
        Bs[3] = Bs[3]- (alpha*dBs[3])
        
        
    
        for i in range(0,3)[::-1]:
        #print(As[i].shape)
            dZ = np.multiply(dAs[i],dRelu(Zs[i]))
            #print(dRelu(Zs[i]))
            dWs[i] = (1/m)* np.dot(dZ,As[i].transpose())
            dBs[i] = (1/m)* np.sum(dZ, axis =1, keepdims = True)
            Ws[i] = Ws[i]- (alpha*dWs[i])
            Bs[i] = Bs[i]- (alpha*dBs[i])
            if i >0:
                dAs[i-1] = np.dot(Ws[i].transpose(),dZ)
    
    print(Ws[3])
    
        #for i in range(numLayers):
            
            
    #print(Ws)
        
"""
    print(As[3][0][100])
    As = []
    As.append(X)
    for i in range(numLayers-1):
        z = (Ws[i] @ As[i]) + Bs[i]
        Zs.append(z)
        a = relu(z)
        As.append(a)

    z = (Ws[3] @ As[3]) + Bs[3]
    Zs.append(z)
    a = sigmoid(z)
    As.append(a)
    current = As[3]
    print(current.shape)
    #for i in range(6000):
    #    if As[4][0][i] != current:
    #        print('different!')
    #        current = As[4][0][i]
        
  """
    
    
    
    
    
    
def main():
    matrixs = matrices()
    X = matrixs[0]
    Y = matrixs[1]
    
    
    
    m = 6000
    numLayers = 4
    alpha = .001
    
    forwardProp(X,Y,m,alpha,numLayers)
    
    
    
    
    
main()


