import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import PathPatch

df =  pd.read_csv("DATA_overlap.csv", names= ['DMP_non_overlap','DMP_overlap','P4_non_overlap','P4_overlap'] )

df = pd.melt(df, var_name="set").dropna()
print(df)

my_pal={"P4_non_overlap":"lightblue", "DMP_non_overlap":"lightgreen", "P4_overlap":"blue", 
"DMP_overlap":"seagreen"}

ax = sns.boxplot(x="set", y='value', data=df, showfliers = False, palette=my_pal)

ax.set(ylim=(0, 1.0))
ax.grid(False)
#plt.legend(fontsize=60)
ax.tick_params(labelsize=15)
ax.set_xlabel("Set",fontsize=20)
ax.set_ylabel("PPV",fontsize=20)
fig = ax.get_figure()
fig.set_figwidth(20)
fig.set_figheight(24)

fig.savefig("Figure_Sup_overlap.png")
plt.show() 
