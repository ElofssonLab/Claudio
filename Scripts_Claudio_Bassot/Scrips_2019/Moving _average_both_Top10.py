from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
colors = 'lightblue'
colors2 = 'salmon'
area = np.pi*3

headers = ['NA','ID','2L','ID.1','Tot','Ratio','coverage']
df = pd.read_csv("Data_1.csv", delimiter=',', names=headers)
df1 = pd.read_csv("Data_20_wo.csv", delimiter=',', names=headers)

print df
plt.scatter(df['Ratio'], df['coverage'], s=area, c=colors, alpha=0.5, label = "E1")
#plt.xscale('log')
#plt.xlim(90,70000)

z = np.polyfit(df['Ratio'], df['coverage'], 1)
p = np.poly1d(z)
plt.plot(df['Ratio'],p(df['Ratio']),"b--")
#df['E1'] = df['coverage'].rolling(window=50).mean()
#plt.plot(df['Ratio'], df['E1'], 'blue')



print df1
plt.scatter(df1['Ratio'], df1['coverage'], s=area, c=colors2, alpha=0.5, label = "E20")
#plt.xscale('log')
#plt.xlim(90,70000)
#df1['E20'] = df1['coverage'].rolling(window=50).mean()
#plt.plot(df1['Ratio'], df1['E20'], 'red')

z = np.polyfit(df1['Ratio'], df1['coverage'], 1)
p = np.poly1d(z)
plt.plot(df1['Ratio'],p(df1['Ratio']),"r--")

plt.legend(loc='upper left')
plt.xlabel('Ratio of Inter Domain contacts')
plt.ylabel('coverage')

plt.show()
