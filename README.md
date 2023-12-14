# Comparative analysis of Machine Learning Algorithms for Phishing URL Detection

# Abstract 


Psh is a type of identity theft that tricks Internet users into disclosing sensitive information such as login credentials, credit/debit card details, and so on.
In recent years, researchers have created a variety of anti-Psh approaches.

However, the problem remains. As a result, with this study, we hope to shed light on this complex subject and give a comparative analysis of defense approaches. This synopsis is divided into five sections. First, we go over the Psh attack's lifecycle in detail, as well as its history and motive. Second, we evaluate the various distribution mechanisms used to disseminate Psh assaults. Finally, we present a taxonomy of several Psh-attacking tactics in desktop and mobile contexts.
Fourth, we compare and contrast various Psh protection techniques.


# Introduction

There are numerous Psh detection apps available. However, unlike predicting spam, only a few experiments have been conducted to compare ML approaches in predicting Psh. The current study analyzes the prediction accuracy of multiple ML approaches for predicting Psh emails, including Logistic Regression (LR), DT(DT), Mlp, Svm (SVM), RFs (RF), XGBoost, and Neural Networks (NNet). The comparison analysis makes use of a data set of 2889 Psh and genuine emails. Furthermore, trained and tested using 43 characteristics.

## About the project


Classification is an important aspect of machine learning; we want to know what class (also known as group) an observation belongs to. The capacity to correctly classify observations is particularly useful in a variety of cyber applications, such as predicting how an attacker will attack or forecasting a Psh technique.

Classification algorithms such as logistic regression, support vector machine, XGBoost, neural network, and DTs are available in data science. The RF clsf, on the other hand, is toward the top of the clsf hierarchy.

In this project, we will do a comparative analysis to determine how the DL algorithm works. And which algorithms are most effective in detecting Psh attacks?


# Observations

To compare the model&#39;s performance, a data frame is created.
The columns of this data frame are the lists created to store the
results of the model.

#Creating dataframe
results = pd.DataFrame({ &#39;ML Model&#39;: ML_Model,
&#39;Train Accuracy&#39;: acc_train,
&#39;Test Accuracy&#39;: acc_test})
results

![image](https://github.com/sanchit-mathr/comparitive-analysis-of-Phishing-link-detector/assets/99555073/ff012bc3-c2dd-41ce-ac2b-0bd805fbdbd5)


#Sorting the datafram on accuracy
results.sort_values(by=[&#39;Test Accuracy&#39;, &#39;Train Accuracy&#39;],
ascending=False)

![image](https://github.com/sanchit-mathr/comparitive-analysis-of-Phishing-link-detector/assets/99555073/5d9b914e-378a-4478-b218-1c791817bc30)

These tables (fig 6.1 and 6.2) are the result of our code-2 where all 10000
URLs are been taken and been selected on a random basis for the phishing
URLs detection test with the help of different models.
Which makes a good call for their comparative analysis, and this table shows
their comparative analysis of the different models chosen, now table 6.1 is
unsorted and table 6.2 is sorted according to the test accuracy.





