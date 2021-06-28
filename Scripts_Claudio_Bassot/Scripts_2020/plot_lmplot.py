import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


df =  pd.read_csv("TM_pcons2.csv")
Set1 = ['blue','green','red']
# Plot sepal with as a function of sepal_length across days
g = sns.lmplot(x="Pcons", y="TM_score", hue="Type", palette=Set1,
                data=df)

# Use more informative axis labels than are provided by default
g.set_axis_labels("Pcons", "TM score")
plt.show()
