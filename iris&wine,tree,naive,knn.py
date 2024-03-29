# -*- coding: utf-8 -*-
"""Iris&Wine,Tree,Naive,KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N8C1QCbx1XSKrL5gChnFeu_hdPAS1ZLq

# Iris & Wine, Compare classifires (Decision Tree, naïve Bayes and k-Nearest neighbors)
"""

import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential, Model
from google.colab import files
from tensorflow.keras.models import model_from_json
from IPython.display import HTML
import sys, os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

"""## Wine"""

wine = datasets.load_wine() #Load data

data=wine['data']
data #Show the numerical data

features_names=wine['feature_names']#Load data about the rows and columns
cultivars = np.array(['Cultivar{}'.format(cl) for cl in wine['target']])#Load cultivar information about each wine
wine_names = np.array(['Wine{}'.format(i) for i in range(data.shape[0])])# Create "nice names" for each row
data = pd.DataFrame(data,columns=features_names,index=wine_names)
data.all()#Check all the columns
#data['total_phenols']

!pip install scprep

import scprep
from scipy.spatial.distance import pdist, squareform
import seaborn as sns
data_scaled = StandardScaler().fit_transform(data)
sns.clustermap(data_scaled, xticklabels=data.columns, row_colors=plt.cm.tab10(wine['target']))
#See the dataset of wine

!pip install pydotplus

"""### Desicion Tree"""

import pandas as pd
import pydotplus #pip install pydotplus
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn import tree

"""#### 50% testing & 50% training"""

# Convert dataset to a frame
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
df_wine['target'] = wine.target
#divide and train
X_train, X_test, y_train, y_test = train_test_split(df_wine.drop('target', axis=1), df_wine['target'], test_size=0.5, random_state=0)
# Define decision tree
clf_tree = tree.DecisionTreeClassifier()#criterion= 'entropy'
# Train model
clf_tree.fit(X_train, y_train)
# Predict
y_pred_tree = clf_tree.predict(X_test)
#Calculate accuracy
accuracy_tree = accuracy_score(y_test, y_pred_tree)
print("Tree accuracy with 50% training and 50% testing:", accuracy_tree)

"""#### 20% testing & 80% training"""

# Convert dataset to a frame
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
df_wine['target'] = wine.target
#divide and train
X_train, X_test, y_train, y_test = train_test_split(df_wine.drop('target', axis=1), df_wine['target'], test_size=0.2, random_state=0)
# Define decision tree
clf_tree = tree.DecisionTreeClassifier()#criterion= 'entropy'
# Train model
clf_tree.fit(X_train, y_train)
# Predict
y_pred_tree = clf_tree.predict(X_test)
#Calculate accuracy
accuracy_tree = accuracy_score(y_test, y_pred_tree)
print("Tree accuracy with 80% training and 20% testing:", accuracy_tree)

# See the tree
import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
tree.plot_tree(clf_tree, filled=True, feature_names=df_wine.drop('target', axis=1).columns)
plt.show()

"""### Naive Bayes"""

from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""#### 20% Test & 80% Train"""

# Convert to Pandas DataSet
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
df_wine['target'] = wine.target
X_train, X_test, y_train, y_test = train_test_split(df_wine.drop('target', axis=1), df_wine['target'], test_size=0.2, random_state=0)
model_gnb = GaussianNB() # Gaussian Naive Bayes
model_mnb = MultinomialNB() # Multinomial Naive Bayes
# Train models
model_gnb.fit(X_train, y_train)
model_mnb.fit(X_train, y_train)
# Predict
y_pred_gnb = model_gnb.predict(X_test)
y_pred_mnb = model_mnb.predict(X_test)
# Calculate Prediction
accuracy_gnb = accuracy_score(y_test, y_pred_gnb)
accuracy_mnb = accuracy_score(y_test, y_pred_mnb)
print("Prediction of Gaussian Naive Bayes:", accuracy_gnb)
print("Prediction of Multinomial Naive Bayes :", accuracy_mnb)

"""#### 50% Test & 50% Train"""

# Convert to Pandas DataSet
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
df_wine['target'] = wine.target
X_train, X_test, y_train, y_test = train_test_split(df_wine.drop('target', axis=1), df_wine['target'], test_size=0.5, random_state=0)
model_gnb = GaussianNB() # Gaussian Naive Bayes
model_mnb = MultinomialNB() # Multinomial Naive Bayes
# Train models
model_gnb.fit(X_train, y_train)
model_mnb.fit(X_train, y_train)
# Predict
y_pred_gnb = model_gnb.predict(X_test)
y_pred_mnb = model_mnb.predict(X_test)
# Calculate Prediction
accuracy_gnb = accuracy_score(y_test, y_pred_gnb)
accuracy_mnb = accuracy_score(y_test, y_pred_mnb)
print("Prediction of Gaussian Naive Bayes:", accuracy_gnb)
print("Prediction of Multinomial Naive Bayes :", accuracy_mnb)

"""###  k-Nearest neighbors

"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""#### 20% Test & 80% Train"""

# Convert the data and target labels to separate variables
X = wine.data
y = wine.target
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# Define the kNN model with k = 5. the best 1-10
knn_model = KNeighborsClassifier(n_neighbors=5)
# Train the model
knn_model.fit(X_train, y_train)
# Predict the labels for the test set
y_pred = knn_model.predict(X_test)
# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of kNN model:", accuracy)

"""#### 50% Test & 50% Train"""

# Convert the data and target labels to separate variables
X = wine.data
y = wine.target
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
# Define the kNN model with k = 5. the best 1-10
knn_model = KNeighborsClassifier(n_neighbors=5)
# Train the model
knn_model.fit(X_train, y_train)
# Predict the labels for the test set
y_pred = knn_model.predict(X_test)
# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of kNN model:", accuracy)

"""## Iris"""

iris = datasets.load_iris()

df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris['target'] = iris.target
iris

"""### Decision Tree

#### 20% Test & 80% Train
"""

X_train, X_test, y_train, y_test = train_test_split(df_iris.drop('target', axis=1), df_iris['target'], test_size=0.2, random_state=0)
# Model
clf_tree = tree.DecisionTreeClassifier(random_state=0)
# Train
clf_tree.fit(X_train, y_train)
# Predict
y_pred_tree = clf_tree.predict(X_test)
# Predict
accuracy_tree = accuracy_score(y_test, y_pred_tree)
print("Predict Decision Tree:", accuracy_tree)

"""#### 50% Test & 50% Train"""

X_train, X_test, y_train, y_test = train_test_split(df_iris.drop('target', axis=1), df_iris['target'], test_size=0.5, random_state=0)
# Model
clf_tree = tree.DecisionTreeClassifier(random_state=0)
# Train
clf_tree.fit(X_train, y_train)
# Predict
y_pred_tree = clf_tree.predict(X_test)
# Predict
accuracy_tree = accuracy_score(y_test, y_pred_tree)
print("Predict Decision Tree:", accuracy_tree)

from sklearn import tree, naive_bayes, neighbors

"""### Naive Bayes

#### 20% Test & 80% Train
"""

X_train, X_test, y_train, y_test = train_test_split(df_iris.drop('target', axis=1), df_iris['target'], test_size=0.2, random_state=0)
# Models
model_gnb = naive_bayes.GaussianNB()
model_mnb = naive_bayes.MultinomialNB()
# Train
model_gnb.fit(X_train, y_train)
model_mnb.fit(X_train, y_train)
# Predict
y_pred_gnb = model_gnb.predict(X_test)
y_pred_mnb = model_mnb.predict(X_test)
# Predict
accuracy_gnb = accuracy_score(y_test, y_pred_gnb)
accuracy_mnb = accuracy_score(y_test, y_pred_mnb)
print("Naive Bayes Gaussiano:", accuracy_gnb)
print("Naive Bayes Multinomial:", accuracy_mnb)

"""#### 50% Test & 50% Train"""

X_train, X_test, y_train, y_test = train_test_split(df_iris.drop('target', axis=1), df_iris['target'], test_size=0.5, random_state=0)
# Models
model_gnb = naive_bayes.GaussianNB()
model_mnb = naive_bayes.MultinomialNB()
# Train
model_gnb.fit(X_train, y_train)
model_mnb.fit(X_train, y_train)
# Predict
y_pred_gnb = model_gnb.predict(X_test)
y_pred_mnb = model_mnb.predict(X_test)
# Predict
accuracy_gnb = accuracy_score(y_test, y_pred_gnb)
accuracy_mnb = accuracy_score(y_test, y_pred_mnb)
print("Naive Bayes Gaussiano:", accuracy_gnb)
print("Naive Bayes Multinomial:", accuracy_mnb)

"""###  k-Nearest neighbors

#### 20% Test & 80% Train
"""

X_train, X_test, y_train, y_test = train_test_split(df_iris.drop('target', axis=1), df_iris['target'], test_size=0.2, random_state=0)
# Model
knn_model = neighbors.KNeighborsClassifier(n_neighbors=5)
# Train
knn_model.fit(X_train, y_train)
# Predict
y_pred_knn = knn_model.predict(X_test)
# Accuracy
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print("Predict KNN:", accuracy_knn)

"""#### 50% Test & 50% Train"""

X_train, X_test, y_train, y_test = train_test_split(df_iris.drop('target', axis=1), df_iris['target'], test_size=0.5, random_state=0)
# Model
knn_model = neighbors.KNeighborsClassifier(n_neighbors=5)
# Train
knn_model.fit(X_train, y_train)
# Predict
y_pred_knn = knn_model.predict(X_test)
# Accuracy
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print("Predict KNN:", accuracy_knn)

"""### Referencias
1. https://colab.research.google.com/github/KrishnaswamyLab/SingleCellWorkshop/blob/master/exercises/Introduction_to_Manifold_Learning/notebooks/00_Answers_Plotting_UCI_wine.ipynb#scrollTo=pRzgHaB6GPRl
2. https://colab.research.google.com/github/daniyal9538/GeneralProjects/blob/master/Decision_Tree_Tutorial.ipynb#scrollTo=6F-M4oVCknRf
3. https://colab.research.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.05-Naive-Bayes.ipynb#scrollTo=Tq9TouuzPbDE
4. https://colab.research.google.com/github/akshayrb22/playing-with-data/blob/master/supervised_learning/KNN/KNN.ipynb


"""