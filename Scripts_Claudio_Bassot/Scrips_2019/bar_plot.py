import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="ticks", palette="pastel")

df =  pd.read_csv("PPV_data_ann3.csv")
df1 = pd.melt(df, id_vars=["Class", "ID"], var_name="Prediction", value_name="PPV")

print df1

diverging_colors = sns.color_palette("RdBu", 6)
my_pal={ "Complete PconsC4":"blue", "Complete GDCA":"crimson","Complete DMP":"green"}


sns.set_style("ticks",{"xtick.major.size": 80, "ytick.major.size": 80})
sns.axes_style("ticks")
ax = sns.boxplot(x="Class", y="PPV", 
            hue="Prediction",  palette=my_pal,
            data=df1, showfliers=False, order=["V.1", "V.2", "V.3", "V.4", "V.5"], linewidth=5)
sns.despine(offset=10, trim=False)


ax.set(ylim=(0, 1.0))
ax.legend_.remove()
ax.tick_params(labelsize=50)
ax.set_xlabel("Class",fontsize=50)
ax.set_ylabel("PPV",fontsize=50)
fig = ax.get_figure()
fig.set_figwidth(40)
fig.set_figheight(24)

fig.savefig("Figure_2D.png")


#plt.show() 
