# -*- coding: utf-8 -*-
"""5  Missing Values.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wsb2P9deBXBsBENmpxaRwbQ-lVi9FUro
"""

#missing values

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("D:\\Course\\Python\\Datasets\\Data.csv")

dataset

X = dataset.iloc[:, :-1].values

X

#y = dataset.iloc[:, 3].values

#y

#Step 1 - Import the method from Libraries

from sklearn.impute import SimpleImputer

# creating a funciton using ur imported Method

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

imputer = imputer.fit(X[:, 1:3])
#imputer

X[:, 1:3] = imputer.transform(X[:, 1:3])

X

dataset = pd.DataFrame(X)

dataset

"""# Other Method to handle the Missing Values"""

data = pd.read_csv("D:\\Course\\Python\\Datasets\\Missing Data.csv")

data

# To check the count of missing values in Each Column

data.apply(lambda x: sum(x.isnull()),axis=0)

# Filling the missing values - age and Salary is continous data type so we will place the missing value with mean

# syntax - Datasetname['Missing value column name'].fillna(mean )
data

# replace missing value with mean in age and Salary

data['Age'].fillna(data['Age'].mean(),inplace = True)
data['Salary'].fillna(data['Salary'].mean(),inplace = True)

data

data['Gender'].mode()

# Replace the Discrete datatype with mode

data['Gender'].fillna(data.Gender.mode()[0],inplace = True)

data

# we can also replace the value manually

test = data['Age'].mean()
test

data['Salary'].fillna(test,inplace=True)
#data['Salary'].fillna(data['Age'].mean(),inplace=True)
#data['salary'].fillna(38.7777778,inplace=True)

data['salary'].fillna(38.7777778,inplace=True)