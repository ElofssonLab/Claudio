import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

features = sys.argv[1]

df = pd.read_csv(features, header = None, names=['Prediction','Tmscore','DS'])
print(df)
# Plot sepal width as a function of sepal_length across days
g = sns.lmplot(x="Prediction", y="Tmscore", hue="DS",
               height=5, data=df)

# Use more informative axis labels than are provided by default
g.set_axis_labels("Predicted TM", "Tmscore")

plt.show() 

