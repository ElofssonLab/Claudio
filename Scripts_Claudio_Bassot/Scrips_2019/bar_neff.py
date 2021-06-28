# library & dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

headers = ["Neff","Set"]
df =  pd.read_csv('Neff_dat.csv', delimiter=',',names=headers)


print df
# Usual boxplot
ax = sns.boxplot(x = "Set",y="Neff", data=df)
 
# Add jitter with the swarmplot function.
ax = sns.swarmplot(x = "Set",y="Neff", data=df, color="grey")
#ax.legend_.remove()
plt.xticks(fontsize=11); plt.yticks(fontsize=11)
plt.xlabel('Set', fontsize=16)
plt.ylabel('Neff', fontsize=16)
plt.show() 
