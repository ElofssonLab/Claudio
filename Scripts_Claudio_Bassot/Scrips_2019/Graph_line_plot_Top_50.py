from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

headers = ['Rank','Inter_GaussDCA_E1','Inter_GaussDCA_E3','Inter_GaussDCA_E10','Inter_GaussDCA_E20','Inter_GaussDCA_E40','Inter_PconsC4_E1','Inter_PconsC4_E3','Inter_PconsC4_E10','Inter_PconsC4_E20','Inter_PconsC4_E40','Intra_GaussDCA_E1','Intra_GaussDCA_E3','Intra_GaussDCA_E10','Intra_GaussDCA_E20','Intra_GaussDCA_E40','Intra_PconsC4_E1','Intra_PconsC4_E3','Intra_PconsC4_E10','Intra_PconsC4_E20','Intra_PconsC4_E40','Intra25_GaussDCA_E1','Intra25_GaussDCA_E3','Intra25_GaussDCA_E10','Intra25_GaussDCA_E20','Intra25_GaussDCA_E40','Intra25_PconsC4_E1','Intra25_PconsC4_E3','Intra25_PconsC4_E10','Intra25_PconsC4_E20','Intra25_PconsC4_E40']
df = pd.read_csv("All_Top_50", delimiter=',', names=headers)
print df
plt.plot(df['Inter_PconsC4_E1'],'b')
plt.plot(df['Inter_PconsC4_E3'],'deepskyblue')
plt.plot(df['Inter_PconsC4_E10'],'darkcyan')
plt.plot(df['Inter_PconsC4_E20'],'darkturquoise')
plt.plot(df['Inter_PconsC4_E40'],'navy')
plt.plot(df['Inter_GaussDCA_E1'], 'red')
plt.plot(df['Inter_GaussDCA_E3'], 'brown')
plt.plot(df['Inter_GaussDCA_E10'],'tomato')
plt.plot(df['Inter_GaussDCA_E20'], 'lightsalmon')
plt.plot(df['Inter_GaussDCA_E40'], 'indianred')
plt.plot(df['Intra_PconsC4_E1'],'b')
plt.plot(df['Intra_PconsC4_E3'],'deepskyblue')
plt.plot(df['Intra_PconsC4_E10'],'darkcyan')
plt.plot(df['Intra_PconsC4_E20'],'darkturquoise')
plt.plot(df['Intra_PconsC4_E40'],'navy')
plt.plot(df['Intra_GaussDCA_E1'], 'red')
plt.plot(df['Intra_GaussDCA_E3'], 'brown')
plt.plot(df['Intra_GaussDCA_E10'],'tomato')
plt.plot(df['Intra_GaussDCA_E20'], 'lightsalmon')
plt.plot(df['Intra_GaussDCA_E40'], 'indianred')
plt.plot(df['Intra25_PconsC4_E1'],'b')
plt.plot(df['Intra25_PconsC4_E3'],'deepskyblue')
plt.plot(df['Intra25_PconsC4_E10'],'darkcyan')
plt.plot(df['Intra25_PconsC4_E20'],'darkturquoise')
plt.plot(df['Intra25_PconsC4_E40'],'navy')
plt.plot(df['Intra25_GaussDCA_E1'], 'red')
plt.plot(df['Intra25_GaussDCA_E3'], 'brown')
plt.plot(df['Intra25_GaussDCA_E10'],'tomato')
plt.plot(df['Intra25_GaussDCA_E20'], 'lightsalmon')
plt.plot(df['Intra25_GaussDCA_E40'], 'indianred')
#['GaussDCA_3'],['GaussDCA_10'],['GaussDCA_20'],['GaussDCA_40'],['PconsC4_1'],['PconsC4_3'],['PconsC4_10'],['PconsC4_20'],['PconsC4_40']
plt.legend(loc='upper right')
plt.xlabel('Rank')
plt.ylabel('PPV')

plt.show()

