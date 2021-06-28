from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
from matplotlib.ticker import PercentFormatter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
colors = 'lightblue'
colors2 = 'salmon'
area = np.pi*3

headers = ['class', 'SS','id','PPV_DMP_inter','CIeD','IC1','PPV_p4_inter','CIeP','IC2','PPV_DMP_intra','CIaD','IaC1','PPV_p4_intra','CIeP','IaC2', 'Ratio']
df = pd.read_csv("ALL_inter_intra.csv", delimiter=',', names=headers)

ax = sns.lmplot(x='Ratio', y='PPV_DMP_inter', data=df, hue_order=["Alpha","Beta","Alpha_Beta"], hue="SS", fit_reg=False, markers=['o','s','p'],legend_out = False)
df['Moving_average'] =  df["PPV_DMP_inter"].groupby(df['SS'], group_keys=False).rolling(10).mean()
groups=df['Moving_average'].groupby(df['SS'])
groups_ratio=df['Ratio'].groupby(df['SS'])
###INTER###
print groups
plt.plot(groups_ratio.get_group('Alpha'), groups.get_group('Alpha'), 'blue',linewidth=4,label = 'Alpha')
plt.plot(groups_ratio.get_group('Beta'), groups.get_group('Beta'), 'orange',linewidth=4, label = 'Beta')
plt.plot(groups_ratio.get_group('Alpha_Beta'), groups.get_group('Alpha_Beta'), 'green',linewidth=4, label = 'Alpha_Beta')

df['Inter'] = df['PPV_DMP_inter'].rolling(window=50).mean()
plt.plot(df['Ratio'], df['Inter'], 'red',linewidth=4, label = 'Total Inter-units')
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
leg = plt.legend()
plt.show()

###INTRA###

ax = sns.lmplot(x='Ratio', y='PPV_DMP_intra', data=df, hue_order=["Alpha","Beta","Alpha_Beta"], hue="SS", fit_reg=False, markers=['o','s','p'],legend_out = False)

df['Moving_average'] =  df["PPV_DMP_intra"].groupby(df['SS'], group_keys=False).rolling(10).mean()
groups=df['Moving_average'].groupby(df['SS'])
groups_ratio=df['Ratio'].groupby(df['SS'])

print groups

plt.plot(groups_ratio.get_group('Alpha'), groups.get_group('Alpha'), 'blue',linewidth=4,label = 'Alpha')
plt.plot(groups_ratio.get_group('Beta'), groups.get_group('Beta'), 'orange',linewidth=4, label = 'Beta')
plt.plot(groups_ratio.get_group('Alpha_Beta'), groups.get_group('Alpha_Beta'), 'green',linewidth=4, label = 'Alpha_Beta')
df['Intra'] = df['PPV_DMP_intra'].rolling(window=50).mean()
plt.plot(df['Ratio'], df['Intra'], 'red',linewidth=4, label = 'Total Inta-units')
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))

plt.xlabel('Ratio Inter/Tot._contacts')
plt.ylabel('PPV')
plt.title("Inter/Intra units contacts ratio")

plt.savefig("Inter_intra_ratio.png")
leg = plt.legend()
plt.show()
