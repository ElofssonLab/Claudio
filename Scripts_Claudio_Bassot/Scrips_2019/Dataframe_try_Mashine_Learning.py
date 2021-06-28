from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df1 = pd.read_csv("all_contact_type6", delimiter=',')
#cols = ['score']
df2= df1[df1['Distance1'] < 20]
df2= df1[df1['Distance2'] < 20]
df3= df2[['Res1','Res2','score','Distance2','Type']]
X = df3.drop(columns = ['Type'])
y = df3['Type']

from sklearn.model_selection import train_test_split#split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)


###KNN###
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier#create new a knn model
knn = KNeighborsClassifier()#create a dictionary of all values we want to test for n_neighbors
params_knn = {'n_neighbors': np.arange(1, 25)}#use gridsearch to test all values for n_neighbors
knn_gs = GridSearchCV(knn, params_knn, cv=5)#fit model to training data
knn_gs.fit(X_train, y_train)
#save best model
knn_best = knn_gs.best_estimator_#check best n_neigbors value
print(knn_gs.best_params_)

####RANDOM FOREST #####
from sklearn.ensemble import RandomForestClassifier#create a new random forest classifier
rf = RandomForestClassifier()#create a dictionary of all values we want to test for n_estimators
params_rf = {'n_estimators': [50, 100, 200]}#use gridsearch to test all values for n_estimators
rf_gs = GridSearchCV(rf, params_rf, cv=5)#fit model to training data
rf_gs.fit(X_train, y_train)
#save best model
rf_best = rf_gs.best_estimator_#check best n_estimators value
print(rf_gs.best_params_)

#Logistic Regression####
from sklearn.linear_model import LogisticRegression#create a new logistic regression model
log_reg = LogisticRegression()#fit the model to the training data
log_reg.fit(X_train, y_train)
#test the three models with the test data and print their accuracy scoresprint
print('knn: {}'.format(knn_best.score(X_test, y_test)))
print('rf: {}'.format(rf_best.score(X_test, y_test)))
print('log_reg: {}'.format(log_reg.score(X_test, y_test)))

#### Voting####
from sklearn.ensemble import VotingClassifier#create a dictionary of our models
estimators=[('knn', knn_best), ('rf', rf_best), ('log_reg', log_reg)]#create our voting classifier, inputting our models
ensemble = VotingClassifier(estimators, voting='hard')
#fit model to training data
ensemble.fit(X_train, y_train)#test our model on the test data
print(ensemble.score(X_test, y_test))


