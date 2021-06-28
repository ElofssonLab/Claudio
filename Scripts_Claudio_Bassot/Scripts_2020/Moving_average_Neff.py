from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
colors = (0,0,0)
area = np.pi*3

headers = ['id','PPV','Neff']
df = pd.read_csv("P4_Neff.csv", delimiter=',', names=headers)
df1 = pd.read_csv("GDCA_Neff.csv", delimiter=',', names=headers)
df3 = pd.read_csv("DMP_Neff.csv", delimiter=',', names=headers)


print df
plt.scatter(df['Neff'], df['PPV'], s=area, c='lightblue', alpha=0.5)
#plt.xscale('log', basex=2)
#plt.xlim(90,70000)
df['PconsC4'] = df['PPV'].rolling(window=50).mean()
plt.plot(df['Neff'], df['PconsC4'], 'blue')
plt.xlabel('Neff')

print df1
plt.scatter(df1['Neff'], df1['PPV'], s=area, c='salmon', alpha=0.5)
#plt.xscale('log', basex=2)
#plt.xlim(90,70000)
df1['GaussDCA'] = df1['PPV'].rolling(window=50).mean()
plt.plot(df1['Neff'], df1['GaussDCA'], 'red')
plt.ylabel('PPV')

print df3
plt.scatter(df3['Neff'], df3['PPV'], s=area, c='lightgreen', alpha=0.5)
#plt.xscale('log', basex=2)
#plt.xlim(90,70000)
df3['DMP'] = df3['PPV'].rolling(window=50).mean()
plt.plot(df3['Neff'], df3['DMP'], 'green')

plt.legend()

plt.show()
