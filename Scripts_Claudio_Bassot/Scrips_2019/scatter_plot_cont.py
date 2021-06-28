from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df1 = pd.read_csv("all_contact_type6", delimiter=',')
#cols = ['score']
df2= df1[df1['score'] > 0.5]
df2= df1[df1['Distance1'] < 20]
df2= df1[df1['Distance2'] < 20]
print df2
#contacts = plt.scatter(df1['Distance1'],df1['Distance2'],c="r")

plot = sns.scatterplot(x='Distance1', y='score', hue="Type", data=df2)

#plt.legend(loc='upper left')
#plt.xlabel('DistanceB')
#plt.ylabel('DistanceA')

fig = plot.get_figure()
fig.savefig("output.png")
