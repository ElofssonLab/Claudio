import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from pprint import pprint


features = sys.argv[1]
test = sys.argv[2]
df = pd.read_csv(features, header = None, names = [
'TM','pcons','local_qm','cbeta_norm_score','interaction_norm_score','packing_norm_score','qmean4_norm_score','qmean6_norm_score','ss_agreement_norm_score','torsion_norm_score','violation','contact_score','E','H','C','L','TOTAL','VDW','BOND','NOE','2.5','3.5','H_conf','E_conf','CONTACTS','SS-NOE','HBONDS','DIHEDRAL','CONTACTS_D','SS-NOE_D','HBONDS_D'], sep =',')
dft = pd.read_csv(test, header = None, names = ['Id','local_qm','cbeta_norm_score','interaction_norm_score','packing_norm_score','qmean4_norm_score','qmean6_norm_score','ss_agreement_norm_score','torsion_norm_score','pcons','violation','contact_score','E','H','C','L','TOTAL','VDW','BOND','NOE','2.5','3.5','H_conf','E_conf','CONTACTS','SS-NOE','HBONDS','DIHEDRAL','CONTACTS_D','SS-NOE_D','HBONDS_D'], sep =',')



pcons = df['pcons']
print(df)


# Labels are the values we want to predict
labels = np.array(df['TM'])
# Remove the labels from the features
# axis 1 refers to the columns
df= df.drop(['TM'], axis = 1)
#df= df.drop('cbeta_norm_score', axis = 1)
dft2 = dft.drop(['Id'], axis = 1)
# Saving feature names for later use
df_list = list(df.columns)
# Convert to numpy array
df = np.array(df)
dft2= np.array(dft2)
#print(dft2)
from sklearn.model_selection import KFold # import KFold

kf = KFold(n_splits=5, random_state = 42, shuffle=True) # Define the split - into 2 folds 
kf.get_n_splits(df) # returns the number of splitting iterations in the cross-validatorprint(kf) KFold(n_splits=2, random_state=None, shuffle=False)


for train_index, test_index in kf.split(df):
	#print('TRAIN:', train_index, 'TEST:', test_index)
	train, test = df[train_index], df[test_index]
	#print(train, labels[train_index])
	train_labels = labels[train_index]
	test_labels = labels[test_index]

from sklearn.model_selection import RandomizedSearchCV# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 300, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(20, 120, num = 10)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [3, 4]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 3]
# Method of selecting samples for training each tree
bootstrap = [True, False]# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
pprint(random_grid)

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()
# Random search of parameters, using 3 fold cross validation, 
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)# Fit the random search model
rf_random.fit(train, train_labels)

def evaluate(model, test, test_labels):
    predictions = model.predict(test)
    errors = abs(predictions - test_labels)
    mape = 100 * np.mean(errors / test_labels)
    accuracy = 100 - mape
    print('Model Performance')
    print('Average Error: {:0.4f} degrees.'.format(np.mean(errors)))
    print('Accuracy = {:0.2f}%.'.format(accuracy))
    
    return accuracy
base_model = RandomForestRegressor(n_estimators = 10, random_state = 42)

base_model.fit(train, train_labels)
base_accuracy = evaluate(base_model, test, test_labels)

best_random = rf_random.best_estimator_
random_accuracy = evaluate(best_random, test, test_labels)

print('Improvement of {:0.2f}%.'.format( 100 * (random_accuracy - base_accuracy) / base_accuracy))
print(rf_random.best_params_)
from sklearn.model_selection import GridSearchCV# Create the parameter grid based on the results of random search 
param_grid = {
    'bootstrap': [True, False],
    'max_depth': [20, 30, 40, 50, 60, 70,80, 90,100,110],
    'max_features': [3,5,10,13,15,20,25,30],
    'min_samples_leaf': [1, 2],
    'min_samples_split': [3, 4],
    'n_estimators': [100,150, 200, 250,300]
}# Create a based model
rf = RandomForestRegressor()# Instantiate the grid search model
grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, 
                          cv = 3, n_jobs = -1, verbose = 2)

# Fit the grid search to the data
grid_search.fit(train, train_labels)
print(grid_search.best_params_)
best_grid = grid_search.best_estimator_
grid_accuracy = evaluate(best_grid, test, test_labels)

print('Improvement of {:0.2f}%.'.format( 100 * (grid_accuracy - base_accuracy) / base_accuracy))

