#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


class Percentron(object):
    
    #epochs迭代次数  ，eta学习速率
    def __init__(self,eta=0.01,epochs=50):
        self.eta = eta 
        self.epochs = epochs
    
    def train(self,X,y):
        
        self.w_ = np.zeros(1 +X.shape[1]) #构造一个矩阵
        self.errors_ = []
        
        for _ in range(self.epochs):
            error = 0 
            for xi,target in zip(X,y): #吧X,y按列组合
                update = self.eta*(target - self.predict(xi))
                self.w_[1:] += update *xi
                self.w_[0] += update
            self.errors_.append(error)
        return self
    
    def net_input(self,X):
        return np.dot(X,self.w_[1:])+ self.w_[0]
    
    def predict(self,X):
        return np.where(self.net_input(X) >= 0.0,1,-1)
    
import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
 
# setosa and versicolor
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
 
# sepal length and petal length
X = df.iloc[0:100, [0,2]].values
 
#%matplotlib inline
import matplotlib.pyplot as plt
from mlxtend.evaluate import plot_decision_regions
'''
ppn = Percentron(epochs=10,eta=0.1)
 
ppn.train(X, y)
print('Weights: %s' % ppn.w_)
plot_decision_regions(X, y, clf=ppn)
plt.title('Perceptron')
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.show()
 
plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
plt.xlabel('Iterations')
plt.ylabel('Missclassifications')
plt.show()
'''
 
# versicolor and virginica
y2 = df.iloc[50:150, 4].values
y2 = np.where(y2 == 'Iris-virginica', -1, 1)
 
# sepal width and petal width
X2 = df.iloc[50:150, [1,3]].values
 
ppn = Percentron(epochs=25,eta=0.01)
ppn.train(X2, y2)
 
plot_decision_regions(X2, y2, clf=ppn)
plt.show()
 
plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
plt.xlabel('Iterations')
plt.ylabel('Missclassifications')
plt.show()
                
    
