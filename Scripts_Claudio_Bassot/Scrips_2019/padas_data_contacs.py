import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Resideus_distance_map_cut.csv', sep=',', header = 0,index_col=0)
cmap = sns.cm.rocket_r
print df
ax = sns.heatmap(df, vmin=3, vmax=7,cmap='Greys_r')
plt.show()    
