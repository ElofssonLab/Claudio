from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
colors = (0,0,0)
area = np.pi*3

#headers = ['id','PPV','Neff','PPV_DMSA']
df = pd.read_csv("MSA_vs_DMP_MSA2.csv", delimiter=',')



plt.scatter(df['Neff'], df['PPV'], s=area, c='lightblue', alpha=0.5)
#plt.xscale('log', basex=2)
#plt.xlim(90,70000)
df['MSA']=df['PPV'].rolling(window=50).mean()
plt.plot(df['Neff'], df['MSA'], 'blue')
plt.xlabel('Neff')

plt.scatter(df['Neff'], df['PPV_DMSA'], s=area, c='salmon', alpha=0.5)
#plt.xscale('log', basex=2)
##plt.xlim(90,70000)
df["Deep MSA"] = df['PPV_DMSA'].rolling(window=50).mean()
plt.plot(df['Neff'], df['Deep MSA'], 'red')
plt.ylabel('PPV')

print df
plt.legend()


plt.show()
