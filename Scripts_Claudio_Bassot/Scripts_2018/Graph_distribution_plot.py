from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats

headers = ['ID','Res1','Res2','Z_score','AA1','A2','Dis','True']
df = pd.read_csv("Total_intra_True8_cont.py", delimiter=' ', names=headers)

sns.distplot(df['Dis'], hist = False, kde = True,
                 kde_kws = {'shade': True, 'linewidth': 3}, 
                  label = 'Intra domain distance')

#['GaussDCA_3'],['GaussDCA_10'],['GaussDCA_20'],['GaussDCA_40'],['PconsC4_1'],['PconsC4_3'],['PconsC4_10'],['PconsC4_20'],['PconsC4_40']

plt.show()

