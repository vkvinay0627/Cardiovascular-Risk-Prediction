from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import plot_roc_curve

from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler

import seaborn as sns 
import matplotlib.pyplot as plt

import numpy as np                               # vectors and matrices
import pandas as pd  

#-----------------------------------------------------------------------------------------------------------------------#
def model_selection(X_train,y_train,X_test,y_test,models):
    accuracies = {}
    recall = {}

    for model in models:
        model_name = str(model).split('.')[-1][:-2]
        print("Model :",model_name)
        model =model().fit(X_train,y_train)
        y_pred = model.predict(X_test)
        acc = model.score(X_test,y_test)*100
        accuracies[model_name] = acc
        print(confusion_matrix(y_test, y_pred))
        print("Accuracy  : ",accuracy_score(y_test, y_pred))
        print("Precision : ",precision_score(y_test, y_pred))
        print("Recall    : ",recall_score(y_test, y_pred))
        print("F1        : ",f1_score(y_test, y_pred))
        rec = (recall_score(y_test, y_pred))
        recall[model_name] = rec*100
        print('-'*50)
#-----------------------------------------------------------------------------------------------------------------------#        
def recall_dict(X_train,y_train,X_test,y_test,models):
    recall = []
    modelnames = []
    for model in models:
        model_name = str(model).split('.')[-1][:-2]
        modelnames.append(model_name)
        model =model().fit(X_train,y_train)
        y_pred = model.predict(X_test)
        rec = (recall_score(y_test, y_pred))
        recall.append(rec)

    recall_list = []
    recall_list.insert(0,modelnames)
    recall_list.insert(1,recall)
#     print(f"before {recall_list}")
    recall_dict = {}
    i = 0
    counter = len(models)
    while i < counter:
        recall_dict[recall_list[0][i]] = recall_list[1][i]
        i+=1
#     print(f"after {recall_dict}")
    
    return recall_dict

def accuracy_dict(X_train,y_train,X_test,y_test,models):
    accuracy = []
    modelnames = []
    for model in models:
        model_name = str(model).split('.')[-1][:-2]
        modelnames.append(model_name)
        model =model().fit(X_train,y_train)
        y_pred = model.predict(X_test)
        acc = model.score(X_test,y_test)
        accuracy.append(acc)

    accuracy_list = []
    accuracy_list.insert(0,modelnames)
    accuracy_list.insert(1,accuracy)
#     print(f"before {accuracy_list}")
    accuracy_dict = {}
    i = 0
    counter = len(models)
    while i < counter:
        accuracy_dict[accuracy_list[0][i]] = accuracy_list[1][i]
        i+=1
#     print(f"after {accuracy_dict}")
    
    return accuracy_dict
#-----------------------------------------------------------------------------------------------------------------------#        
def recall_plots(recall):
    colors = ["purple", "green", "orange", "magenta"]
    
    sns.set_style("whitegrid")
    plt.figure(figsize=(16,5))
    plt.yticks(np.arange(0,100,5))
    plt.ylabel("Recall %")
    plt.xlabel("Algorithms")
    sns.barplot(x=list(recall.keys()), y=list(recall.values()), palette=colors)
    plt.show()
    
def accuracy_plots(accuracies):
    colors = ["purple", "green", "orange", "magenta"]

    sns.set_style("whitegrid")
    plt.figure(figsize=(16,5))
    plt.yticks(np.arange(0,100,5))
    plt.ylabel("Accuracy %")
    plt.xlabel("Algorithms")
    sns.barplot(x=list(accuracies.keys()), y=list(accuracies.values()), palette=colors)
    plt.show()
#-----------------------------------------------------------------------------------------------------------------------#    
    

