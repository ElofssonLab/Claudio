import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib
from sklearn.linear_model import LinearRegression

df = pd.read_csv("Data_all_features.3.0.csv", sep=',',)
#dft = pd.read_csv("TM_Qmean_unknow", header = 0)
#print(df['violation'])
#pcons = df['Pcons']

# Labels are the values we want to predict
labels = np.array(df['tmalign'])
# Remove the labels from the features
# axis 1 refers to the columns
df= df.drop('modelID', axis = 1)
dft= df.drop('tmalign', axis = 1)


print(df) 
###old
#X = df.iloc[:, :-1].values
#y = df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Linear Regression

#Random Forest Regression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn.model_selection import KFold 

kf = KFold(n_splits=5, random_state = 42,  shuffle=True) # Define the split - into 2 folds 
kf.get_n_splits(df) # returns the number of splitting iterations in the cross-validatorprint(kf) KFold(n_splits=2, random_state=None, shuffle=False)

regressor = RandomForestRegressor(n_estimators = 200, max_depth  = 90, random_state = 42)

for train_index, test_index in kf.split(dft):
	#print('TRAIN:', train_index, 'TEST:', test_index)
	train, test = df[train_index], df[test_index]
	#print(train, labels[train_index])

	rf.fit(train, labels[train_index]);
	predictions = rf.predict(test)
	errors = abs(predictions - labels[test_index])
	print('Mean Absolute Error:', round(np.mean(errors), 5), 'TM point.')
	mape = 100 * (errors / labels[test_index])# Calculate and display accuracy
	accuracy = 100 - np.mean(mape)
	MAE = mean_squared_error(labels[test_index], predictions)
	#print('MAE',MAE,)



