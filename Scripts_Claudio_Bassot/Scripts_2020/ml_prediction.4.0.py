import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

features = sys.argv[1]
test = sys.argv[2]
df = pd.read_csv(features, header = None, names = [
'TM','pcons','local_qm','cbeta_norm_score','interaction_norm_score','packing_norm_score','qmean4_norm_score','qmean6_norm_score','ss_agreement_norm_score','torsion_norm_score','violation','contact_score','E','H','C','L','TOTAL','VDW','BOND','NOE','2.5','3.5','H_conf','E_conf','CONTACTS','SS-NOE','HBONDS','DIHEDRAL','CONTACTS_D','SS-NOE_D','HBONDS_D'], sep =',')
dft = pd.read_csv(test, header = None, names = ['Id','local_qm','cbeta_norm_score','interaction_norm_score','packing_norm_score','qmean4_norm_score','qmean6_norm_score','ss_agreement_norm_score','torsion_norm_score','pcons','violation','contact_score','E','H','C','L','TOTAL','VDW','BOND','NOE','2.5','3.5','H_conf','E_conf','CONTACTS','SS-NOE','HBONDS','DIHEDRAL','CONTACTS_D','SS-NOE_D','HBONDS_D'], sep =',')

pcons = df['pcons']


# Labels are the values we want to predict
labels = np.array(df['TM'])
# Remove the labels from the features
# axis 1 refers to the columns
df= df.drop([
'TM','qmean4_norm_score','qmean6_norm_score','torsion_norm_score','E','H','TOTAL','VDW','NOE','2.5','3.5','H_conf','CONTACTS','SS-NOE','DIHEDRAL','CONTACTS_D','SS-NOE_D','HBONDS_D'], axis = 1)
#df= df.drop('cbeta_norm_score', axis = 1)
dft2 = dft.drop(['Id','qmean4_norm_score','qmean6_norm_score','torsion_norm_score','E','H','TOTAL','VDW','NOE','2.5','3.5','H_conf','CONTACTS','SS-NOE','DIHEDRAL','CONTACTS_D','SS-NOE_D','HBONDS_D'], axis = 1)
# Saving feature names for later use
df_list = list(df.columns)
# Convert to numpy array
print(df)
df = np.array(df)
dft2= np.array(dft2)
#print(dft2)
from sklearn.model_selection import KFold # import KFold

kf = KFold(n_splits=5, random_state = 42,  shuffle=True) # Define the split - into 2 folds 
kf.get_n_splits(df) # returns the number of splitting iterations in the cross-validatorprint(kf) KFold(n_splits=2, random_state=None, shuffle=False)

rf = RandomForestRegressor(n_estimators = 240,max_depth = 60, random_state = 42)

for train_index, test_index in kf.split(df):
	#print('TRAIN:', train_index, 'TEST:', test_index)
	train, test = df[train_index], df[test_index]
	#print(train, labels[train_index])
	
	rf.fit(train, labels[train_index]);
	predictions = rf.predict(test)
	errors = abs(predictions - labels[test_index])
	#print('Mean Absolute Error:', round(np.mean(errors), 2), 'TM point.')
	mape = 100 * (errors / labels[test_index])# Calculate and display accuracy
	accuracy = 100 - np.mean(mape)
	MAE = mean_squared_error(labels[test_index], predictions)
	#print('MAE',MAE,)
	print('Accuracy:', round(accuracy, 2), '%.')

	Pred_TM =[predictions, labels[test_index]]
	#for v in zip(*Pred_TM):
        #	print(*v)


### Feature Importance ####

importances = rf.feature_importances_
std = np.std([tree.feature_importances_ for tree in rf.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(df.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

######Final Model
kf2 = KFold(n_splits=815, random_state = 42,  shuffle=True) # Define the split - into 2 folds 
rf2 = RandomForestRegressor(n_estimators = 240, random_state = 42)


for train_index, test_index in  kf2.split(df):
	#print('TRAIN:', train_index, 'TEST:', test_index)
	train, test = df[train_index], df[test_index]
	#print(train, labels[train_index])
	rf2.fit(train, labels[train_index]);

#test
from sklearn.externals import joblib
joblib.dump(rf2, 'QA_fit2')

fittedModel = joblib.load('QA_fit2')
result = fittedModel.predict(dft2)

#print(result)
df3 = pd.DataFrame(result)
#print(dft)
#print(df3)

for v in zip(*Pred_TM):
        print (*v)

df3 = df3.assign(Id = dft['Id'].values)
df3["predicted_TM"] = result

print(df3)




