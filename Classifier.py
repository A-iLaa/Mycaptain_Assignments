# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZqkTv2l1vo1d1fXno5puXHa_b5U-qdTj
"""

#importing Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,recall_score

#Reading Dataset
df=pd.read_csv("diabetes.csv")
df.head()

#droping skin thickness column as it wont effect the output
df=df.drop("SkinThickness",axis=1)

#changing the column names
df.columns=["pregnant","glucose","bp","glucose","bmi","pedigree","age","label"]
df.head()

#sliting dependent and independent data
X=df.drop("label",axis=1)
y=df.label

#spliting training and testing data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=43)

#building model using Random Forest
rf=RandomForestClassifier()
rf.fit(X_train,y_train)

#predicting output for test data
y_pred=rf.predict(X_test)

#Evaluating the model
print("Confusion Matrix:  ", confusion_matrix(y_test,y_pred))
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Recall:",recall_score(y_test,y_pred))

#Evaluating the model
print("Confusion Matrix:  ", confusion_matrix(y_test,y_pred))
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Recall:",recall_score(y_test,y_pred))

#building model using logistic regression
lr=LogisticRegression()
lr.fit(X_train,y_train)

#predicting output for test data
y_pred=lr.predict(X_test)

#Evaluating the model
print("Confusion Matrix:  ", confusion_matrix(y_test,y_pred))
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Recall:",recall_score(y_test,y_pred))