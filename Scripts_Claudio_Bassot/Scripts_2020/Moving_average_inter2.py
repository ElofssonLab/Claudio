from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
from matplotlib.ticker import PercentFormatter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#colors = 'lightblue'
#colors2 = 'salmon'
area = np.pi*3

headers = ['class','type','id','PPV_DMP_inter','CIeD','IC1','PPV_p4_inter','CIeP','IC2','PPV_DMP_intra','CIaD','IaC1','PPV_p4_intra','CIeP','IaC2', 'Ratio']
df = pd.read_csv("ALL_inter_intra.csv", delimiter=',', names=headers)

print df

#plt.scatter(df['Ratio'], df['PPV_DMP_intra'], s=area, c=colors2, alpha=0.5)
#plt.xscale('log', basex=2)
#plt.xlim(90,70000)
ax = sns.lmplot(x='Ratio', y='PPV_DMP_intra', data=df, hue_order=['III.1','III.2','III.3','III.4','III.5','IV.1','IV.2','IV.3','IV.4','IV.5','IV.6','IV.7','IV.8','IV.9','IV.10','V.1','V.2','V.3','V.4','V.5'], hue="class",  fit_reg=False, markers=['o','s','p','x','+','*','<','D','h','>',',','v','1','2','3','4','8','P','H','|'])
df['Intra'] = df['PPV_DMP_intra'].rolling(window=50).mean()
plt.plot(df['Ratio'], df['Intra'], 'red')
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))

#plt.scatter(df['Ratio'], df['PPV_DMP_inter'], s=area, c=colors, alpha=0.5)
#plt.xscale('log', basex=2)
ax = sns.lmplot(x='Ratio', y='PPV_DMP_inter', data=df, hue_order=['III.1','III.2','III.3','III.4','III.5','IV.1','IV.2','IV.3','IV.4','IV.5','IV.6','IV.7','IV.8','IV.9','IV.10','V.1','V.2','V.3','V.4','V.5'], hue="class", fit_reg=False, markers=['o','s','p','x','+','*','<','D','h','>',',','v','1','2','3','4','8','P','H','|'])
df['Inter'] = df['PPV_DMP_inter'].rolling(window=50).mean()
plt.plot(df['Ratio'], df['Inter'], 'blue')
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))


#plt.legend(loc='best')
plt.xlabel('Ratio Inter/Tot._contacts')
plt.ylabel('PPV')
plt.title("Inter/Intra units contacts ratio")

plt.savefig("Inter_intra_ratio.png")
plt.show()
