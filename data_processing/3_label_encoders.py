# -*- coding: utf-8 -*-
"""3. Label Encoders.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LWMTfP0xZbdLPjDamPbkn8VISSvql0mC
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:\\Course\\Python\\Datasets\\Churn_Modelling.csv")

dataset

X = dataset.iloc[:, 3:13].values
X
y = dataset.iloc[:, 13].values
y

X

X

test1 = pd.DataFrame(X)
test1

from sklearn.preprocessing import LabelEncoder, OneHotEncoder # import methods and Libraries

# Converting the categorical data into Number (0 ,1 ,2)
# create a function using imported

labelencoder_X_1 = LabelEncoder()

X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])

# .fit() - will apply the function on data
#TransforM() - will convert the data into required values
# labelencoder_X_1.fit((X[:, 1]))
#labelencoder_X_1.Transform((X[:, 1]))
# .fit_Transform() : It will apply and convert the values into required format

labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])

X
test2 = pd.DataFrame(X)
test2

# Creating 3 dummy varabiles for country ( Factor level of 3 spain , France and Germany)

#onehotencoder = OneHotEncoder()
#X = onehotencoder.fit_transform(X).toarray()
#X = X[:, 1:]


#onehotencoder = OneHotEncoder()
#X = onehotencoder.fit_transform(X).toarray()
#X = X[:, 1:]

# column Transformer method is used to convert the data which is more than 2 factor level


from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([("Geography", OneHotEncoder(), [1])])

X = ct.fit_transform(X)

abc=pd.DataFrame(X)
abc

# label Encoder - will convert the datainto 0 and 1 ( factor level 2)
# Onehot encoder and Column Transfer - will helps to  create the dummy variable( more than 2 factor
                                   #leve) and convert the data into 0 and 1