# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vLt6slZE6JUCZeqgPqpo1-e6Kz4pHsa3
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.datasets import load_iris
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
iris = load_iris()
sns.boxplot(data=iris.data,width=0.5,fliersize=6)
sns.set(rc ={'figure.figsize':(2,5)})
x = iris.data
y = iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.5)
'''
#DecisionTreeClassifier
my_classifier=  tree.DecisionTreeClassifier()
my_classifier = my_classifier.fit(x_train,y_train)
prediction = my_classifier.predict(x_test)
print(accuracy_score(y_test,prediction))
'''
'''
#LinearRegression
my_classifier=  LinearRegression()
my_classifier = my_classifier.fit(x_train,y_train)
prediction = my_classifier.predict(x_test)
print(accuracy_score(y_test,prediction))
'''
'''
#LogisticRegression
my_classifier=  LogisticRegression()
my_classifier = my_classifier.fit(x_train,y_train)
prediction = my_classifier.predict(x_test)
print(accuracy_score(y_test,prediction))
'''
'''
#RandomForestClassifier
my_classifier=  RandomForestClassifier()
my_classifier = my_classifier.fit(x_train,y_train)
prediction = my_classifier.predict(x_test)
print(accuracy_score(y_test,prediction))
'''
#KNeighborsClassifier
my_classifier=  KNeighborsClassifier()
my_classifier = my_classifier.fit(x_train,y_train)
prediction = my_classifier.predict(x_test)
print(accuracy_score(y_test,prediction))