from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
from matplotlib.ticker import PercentFormatter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
colors = 'lightblue'
colors2 = 'salmon'
#colors3 = 'orange'
#colors4 = 'brown'
area = np.pi*3

headers = ['class','id','PPV_DMP_inter','CIeD','IC1','PPV_p4_inter','CIeP','IC2','PPV_DMP_intra','CIaD','IaC1','PPV_p4_intra','CIeP','IaC2', 'Ratio']
df = pd.read_csv("ALL_inter_intra.csv", delimiter=',', names=headers)
#W"df1 = pd.read_csv("Intra_ratio.csv", delimiter=',', names=headers)


print df
plt.scatter(df['Ratio'], df['PPV_DMP_inter'], s=area, c=colors, alpha=0.5)
#plt.xscale('log', basex=2)

df['Inter_DMP'] = df['PPV_DMP_inter'].rolling(window=50).mean()
plt.plot(df['Ratio'], df['Inter_DMP'], 'blue')
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))

#plt.scatter(df['Ratio'], df['PPV_p4_inter'], s=area, c=colors, alpha=0.5)
#plt.xscale('log', basex=2)
#plt.xlim(90,70000)
#df['Inter_P4'] = df['PPV_p4_inter'].rolling(window=50).mean()
#plt.plot(df['Ratio'], df['Inter_P4'], 'blue')

plt.scatter(df['Ratio'], df['PPV_DMP_intra'], s=area, c=colors2, alpha=0.5)
#plt.xscale('log', basex=2)

df['Intra_DMP'] = df['PPV_DMP_intra'].rolling(window=50).mean()
plt.plot(df['Ratio'], df['Intra_DMP'], 'red')
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))

#plt.scatter(df['Ratio'], df['PPV_p4_intra'], s=area, c=colors2, alpha=0.5)
#plt.xscale('log', basex=2)
#plt.xlim(90,70000)
#df['Intra'] = df['PPV_p4_intra'].rolling(window=50).mean()
#plt.plot(df['Ratio'], df['Intra'], 'green')

plt.legend(loc='best')
plt.xlabel('Ratio Inter/Tot._contacts')
plt.ylabel('PPV')
plt.title("Inter/Intra units contacts ratio")

plt.savefig("Inter_intra_ratio.png")
plt.show()
