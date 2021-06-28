import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks", palette="pastel")

df =  pd.read_csv("TM_score_unit3.csv")
df1 = pd.melt(df, id_vars=["Class", "ID"], var_name="Model", value_name="TM score")
df2 =  pd.read_csv("TM_score_unit3.csv")
df3 = pd.melt(df2, id_vars=["Class", "ID"], var_name="Model", value_name="TM score")
my_pal={"Single unit":"g", "Single unit modelled together with the complete repeat region":"orange"}
#Single unit modeled with the complete region
concatenated = pd.concat([df1, df3])
print df1
ax = sns.boxplot(x="Class", y="TM score",
            hue="Model",  palette=my_pal,
            data=concatenated, showfliers=False, order=["V.1", "V.2", "V.3", "V.4", "V.5"])
sns.despine(offset=10, trim=False)

sns.set(font_scale=1.4)
ax.set(ylim=(0, 1.0))

#ax.legend_.remove()
plt.show() 
