import argparse
import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

features = sys.argv[1]
test = sys.argv[2]
df = pd.read_csv(features, header = None, names = ['TM','pcons','local_qm'], sep =',')
dft = pd.read_csv(test, header = None, names = ['Id', 'pcons','local_qm'], sep =',')
# Create the model with 100 trees
print(df)
# Labels are the values we want to predict
labels = np.array(df['TM'])
# Remove the labels from the features
# axis 1 refers to the columns
df= df.drop('TM', axis = 1)
dft2=dft.drop('Id',axis =1)
# Saving feature names for later use
df_list = list(df.columns)
# Convert to numpy array
df = np.array(df)
dft2= np.array(dft2)
#print(dft2)
# Using Skicit-learn to split data into training and testing sets
from sklearn.model_selection import train_test_split
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(df, labels, test_size = 0.25, random_state = 42)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
#print(test_features)
#print(dft2)
print('Testing Labels Shape:', test_labels.shape)

# The baseline predictions are the historical averages
#baseline_preds = test_features[:, df_list.index('sum')]
# Baseline errors, and display average baseline error
#baseline_errors = abs(baseline_preds - test_labels)
#print('Average baseline error: ', round(np.mean(baseline_errors), 2))

# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 100, random_state = None)
# Train the model on training data
rf.fit(train_features, train_labels);

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'TM point.')

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / test_labels)# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')

#test
from sklearn.externals import joblib
joblib.dump(rf, 'QA_fit')

fittedModel = joblib.load('QA_fit')
result = fittedModel.predict(dft2)

print(result)
df3 = pd.DataFrame(result)
print(dft)
print(df3)

Pred_TM =[predictions,test_labels]

#for v in zip(*Pred_TM):
#        print (*v)

#df3 = df3.assign(Id = dft['Id'].values)
#df3["predicted_TM"] = result

#print(df3)




