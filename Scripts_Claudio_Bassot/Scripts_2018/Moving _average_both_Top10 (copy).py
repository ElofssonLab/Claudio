from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
colors = (0,0,0)
area = np.pi*3

headers = ['id','PPV','N_seq']
df = pd.read_csv("Top_10_hh20_p4", delimiter=',', names=headers)
df1 = pd.read_csv("Top_10_hh20_gdca", delimiter=',', names=headers)

print df
plt.scatter(df['N_seq'], df['PPV'], s=area, c=colors, alpha=0.5)
plt.xscale('log')
plt.xlim(90,70000)
df['PcosnC4'] = df['PPV'].rolling(window=50).mean()
plt.plot(df['N_seq'], df['PcosnC4'], 'blue')

print df1
plt.scatter(df1['N_seq'], df1['PPV'], s=area, c=colors, alpha=0.5)
plt.xscale('log')
plt.xlim(90,70000)
df1['GaussDCA'] = df1['PPV'].rolling(window=50).mean()
plt.plot(df1['N_seq'], df1['GaussDCA'], 'red')

plt.legend(loc='upper left')
plt.xlabel('Number of sequences')
plt.ylabel('PPV')

plt.show()
