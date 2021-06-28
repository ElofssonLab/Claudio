from matplotlib import rcParams, cycler
from matplotlib.lines import Line2D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

headers = ['Contacs','True_Predicted_Inter_Contacs','False_Predicted_Inter_Contacs','True_Predicted_Intra_Contacs','False_Predicted_Intra_Contacs','Inter_Contacs','Intra_Contacs']
df = pd.read_csv("matrix_contact_%.csv", delimiter=',', names=headers)
print df
#plt.plot(df['True_Predicted_Inter_Contacs'], 'red')
#plt.plot(df['False_Predicted_Inter_Contacs'],'b')
#plt.plot(df['True_Predicted_Intra_Contacs'],'green')
#plt.plot(df['False_Predicted_Intra_Contacs'],'purple')
plt.plot(df['Inter_Contacs'],'red')
plt.plot(df['Intra_Contacs'],'blue')


#['GaussDCA_3'],['GaussDCA_10'],['GaussDCA_20'],['GaussDCA_40'],['PconsC4_1'],['PconsC4_3'],['PconsC4_10'],['PconsC4_20'],['PconsC4_40']
plt.legend(loc='down left')
plt.xlabel('contacts_pattern')
plt.ylabel('Log_contacs_number')

plt.show()

