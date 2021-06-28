import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

# Create data
headers = ['Type','ID','TM','pcons']

df = pd.read_csv("TM_pcons_data_DMP.csv", delimiter=',', names=headers)

# Prepare Data 
# Create as many colors as there are unique midwest['Type']
#categories = np.unique(df['Type'])
#colors = [plt.cm.tab20(i/float(len(categories)-1)) for i in range(len(categories))]

# Draw Plot for Each Type
#plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')
ax = sns.lmplot(x='pcons', y='TM', data=df, hue="Type",fit_reg=False, markers=['o','s','p','x','+','*','<','D','h','>',',','v','1','2','3','4','8','P','H','|'])

#for i, Type in enumerate(categories):
#    print Type
#    plt.scatter('pcons', 'TM',
#                data=df.loc[df.Type==Type, :], 
#                s=50, c=colors[i], label=str(Type))

# Decorations
#plt.gca().set(xlim=(0.0, 1), ylim=(0, 1),
#              xlabel='Pcons', ylabel='TM',)

plt.xticks(fontsize=11); plt.yticks(fontsize=11)
plt.xlabel('Pcons', fontsize=16)
#plt.set_xticks(['0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8'])
#plt.set_xticklabels(['0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8'])
#plt.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
#plt.xaxis.set_major_formatter(ticker.ScalarFormatter())
plt.ylabel('TM', fontsize=16)
#plt.title("DATA All Repeats", fontsize=22)
#plt.legend(fontsize=14)    

plt.figure(facecolor="white")
plt.show()    

