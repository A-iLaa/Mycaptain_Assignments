# -*- coding: utf-8 -*-
"""Logistic Regression with Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tJlTqByGzVd_-EpqRcG4KHrMIrb2Bb97
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')

### Predict survival on the Titanic ship
### Given a passenger data , can we predict if he can survive or not

train = pd.read_csv('titanic_train.csv')
train.head()

train.shape

train.sample(n=500)

train.info()

train.shape

train.describe()

train.describe(include=object)

train.isnull().sum()

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

percent_missing=train.isnull().sum()*100/len(train)
percent_missing

missing_perct_df=pd.DataFrame({"col_name":train.columns,"% missing":percent_missing})
# missing_perct_df.head(11)
missing_perct_df.sort_values(by="% missing",ascending=False)

train.isnull().sum()

"""Roughly 20 percent of the Age data is missing. The proportion of Age missing is likely small enough for reasonable replacement with some form of imputation. Looking at the Cabin column, it looks like we are just missing too much of that data"""

sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train,palette='RdBu_r')

# Above plot says that nonsurvied is more than survive

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')

#Insght: as we can see female tends to survive more than males.

sns.set_style('whitegrid')
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')

sns.distplot(train['Age'].dropna(),kde=True,color='darkred',bins=30)

train['Age'].hist(bins=30,color='darkred',alpha=0.7)

sns.countplot(x='SibSp',data=train)

train['Fare'].hist(color='green',bins=40,figsize=(8,4))

"""___
## Data Cleaning
We want to fill in missing age data instead of just dropping the missing age data rows. One way to do this is by filling in the mean age of all the passengers (imputation).


"""

plt.figure(figsize=(12, 7))
sns.boxplot(x='Pclass',y='Age',data=train,palette='tab10')

train.head()

# 37,29 and 24 are median values of class1,2, and 3

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age

"""Now apply that function!"""

train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)
train.head()

"""Now let's check that heat map again!"""

sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

train.info()

"""Drop the Cabin column and the row in Embarked that is NaN."""

train.drop('Cabin',axis=1,inplace=True)

train.head()

train.dropna(inplace=True)

"""## Converting Categorical Features"""

train.info()

train["Sex"].value_counts()

train["Embarked"].value_counts()

train.head()

sex = pd.get_dummies(train['Sex'],drop_first=True)
sex

embark = pd.get_dummies(train['Embarked'],drop_first=True)

embark.head()

train.head(11)

train.drop(['PassengerId','Sex','Embarked','Name','Ticket'],axis=1,inplace=True)

train.head()

train = pd.concat([train,sex,embark],axis=1)

train.head(11)

train.shape

"""

# Building a Logistic Regression model


## Train Test Split"""

from sklearn.model_selection import train_test_split

train.shape

X_train, X_test, y_train, y_test = train_test_split(train.drop('Survived',axis=1),
                                         train['Survived'], test_size=0.30,
                                                    random_state=76)

train.head()

X_train.head()

X_train.shape

X_train.head()

X_train.head()

y_test.head()

"""## Training and Predicting"""

# 1.import the model from sklearn
from sklearn.linear_model import LogisticRegression

# 2.Initilize
logmodel = LogisticRegression()

# 3.train
logmodel.fit(X_train,y_train)


# 4.predict
predictions = logmodel.predict(X_test)

predictions[:5]

predictions_prob = logmodel.predict_proba(X_test)
predictions_prob

"""Let's move on to evaluate our model!

## Evaluation

We can check precision,recall,f1-score using classification report!
"""

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

results = confusion_matrix(y_test, predictions)

results

accuracy_score(y_test, predictions)

y_test[:10]

predictions[:10]

print(classification_report(y_test,predictions))

