# Cardiovascular-Risk-Prediction



# Introduction : 

Heart disease is the major cause of morbidity and mortality globally: it accounts for more deaths annually than any other cause. According to the WHO, an estimated 17.9 million people died from heart disease in 2016, representing 31% of all global deaths.

Doctors and scientists alike have turned to machine learning (ML) techniques to develop screening tools and this is because of their superiority in pattern recognition and classification as compared to other traditional statistical approaches.


## Problem Statement:

The dataset is from an ongoing cardiovascular study on
 residents of the town of Framingham, Massachusetts.
  The classification goal is to predict whether the
   patient has a 10-year risk of future coronary heart 
   disease (CHD). The dataset provides the patients’ 
   information. It includes over 4,000 records and 15
    attributes.



## Results

Algorithms|Recall

LogisticRegression|0.72

GaussianNB|0.28

KNeighborsClassifier|0.54

DecisionTreeClassifier|0.36



![Screenshot (528)](https://user-images.githubusercontent.com/48415899/154743096-f8e2c0c0-d78f-4bb0-b890-b86d103f907f.png)


## Conclusion
Our issue statement involves medical concerns, we must emphasise the recall (false negative) performance matrix above other performance matrixes such as accuracy, F1, and so on.

We used GridsearchCV to do hyperparameter optimization and tweak our model to achieve the best possible outcome and were able to raise recall to 0.80 for KNeighborsClassifier.

![Screenshot (529)](https://user-images.githubusercontent.com/48415899/154746523-044b7945-506f-40ca-a8de-359bddc4b8f1.png)
)
