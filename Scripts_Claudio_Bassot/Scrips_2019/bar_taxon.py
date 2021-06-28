import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv("organism.csv")
print df


ax = sns.barplot(x="Kingdom", y="Unknown vs PDB dataset", data=df)
sns.despine(offset=10, trim=False)


sns.set(font_scale=4)
for item in ax.get_xticklabels():
    item.set_rotation(90)
#ax.legend_.remove()
#fig = plt.gcf()
#fig.set_size_inches(20, 24)
plt.xticks(fontsize=14); plt.yticks(fontsize=14)
plt.xlabel('Kingdoms', fontsize=16)
plt.ylabel('Variation between datasets', fontsize=16)
plt.savefig("taxon.png", dpi=300)
plt.subplots_adjust(bottom=0.35)
plt.show()

