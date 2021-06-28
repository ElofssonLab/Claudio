import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks", palette="pastel")

df =  pd.read_csv("TM_data.csv")
df1 = pd.melt(df, id_vars=["Class", "ID"], var_name="Model", value_name="TM score")
my_pal={"Single unit Pconsc4":"lightblue", "Single unit DMP":"yellow" , "Double units Pconsc4":"blue" , "Double units DMP":"orange", "Compleate DMP":"peru", "Compleate PconsC4":"darkblue"}
print df1
ax = sns.boxplot(x="Class", y="TM score", hue="Model",  palette=my_pal, data=df1, showfliers=False, order=["IV.6", "IV.7", "IV.8", "IV.9", "IV.10"])
sns.despine(offset=10, trim=False)

sns.set(font_scale=1.4)
ax.set(ylim=(0, 1.0))

#ax.legend_.remove()
plt.show() 
