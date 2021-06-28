import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
#sns.set(style="ticks", palette="pastel")

df =  pd.read_csv("RMSD2.csv",sep =',')
#df['RMSD']=df['RMSD'].fillna(method='ffill')
print df
RH1 = range(112,137) 
RH2 = range(173,196)

clrs = ['white' if (x in RH1) or (x in RH2) else 'blue' for x in df['res'] ]
print clrs
#sns.set_style("ticks",{"xtick.major.size": 80, "ytick.major.size": 80})
#sns.axes_style("ticks")
ax = sns.lineplot(x='res', y="RMSD",
            data=df, palette=clrs,)
#sns.despine(offset=10, trim=False)

#ax.set(ylim=(0, 1.0))
#ax.legend_.remove()
ax.tick_params(labelsize=10)
##ax.set_xlabel("Residues",fontsize=20)
#ax.set_ylabel("RMSD",fontsize=20)

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
#fig = ax.get_figure()
#fig.set_figwidth(40)
#fig.set_figheight(24)

#fig.savefig("Figure_2D.png")


ax.plt.show() 
