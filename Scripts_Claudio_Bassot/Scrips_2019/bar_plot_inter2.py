import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
sns.set(style="ticks", palette="pastel")

df =  pd.read_csv("inter_intra.csv")
df1 = pd.melt(df, id_vars=["Class", "ID"], var_name="Prediction", value_name="PPV")

print df1


my_pal={"PPV_intra_unit_pconsc4":"c", "PPV_Inter_unit_pconsc4":"blue", "PPV_Intra_unit_gDCA":"lightcoral", "PPV_Inter_unit_gDCA":"crimson"}


ax = sns.boxplot(x="Class", y="PPV",
            hue="Prediction",  palette=my_pal,
            data=df1,showfliers=False, order=["V.1", "V.2", "V.3", "V.4", "V.5"])
sns.despine(offset=10, trim=False)


sns.set(font_scale=1.4)
ax.set(ylim=(0, 1.0))

#ax.legend_.remove()
fig = plt.gcf()
fig.set_size_inches( 16, 10)
plt.savefig("interBA.png", dpi=300)
