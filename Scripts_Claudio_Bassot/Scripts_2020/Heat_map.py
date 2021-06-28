import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
from pandas import DataFrame 
sns.set()

heat=sys.argv[1]

# Load the example flights dataset and conver to long-form
Cov = pd.read_csv(heat, sep=',',header=0,index_col=0)
print Cov
#df2 = DataFrame(Cov.values, columns=cols, index=index)
#print(df2)
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
vmin = 0.000000003
vmax = 1
sns.clustermap(data=Cov,cmap="rainbow",center=0.35, vmax=0.7, vmin=0)
plt.yticks(rotation=0) 
plt.show()
