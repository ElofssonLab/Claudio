import sys
import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

# Create data
headers = ['Type','ID','TM','pcons']

df = pd.read_csv("DATA_optimum.csv", delimiter=' ', names=headers)

# Draw Plot for Each Type

Single_Unit, Single_Unit_std = (0.307, 0.168, 0.188, 0.446, 0.184, 0.197,0.369, 0.245, 0.203, 0.394, 0.681,0.310, 0.305, 0.366, 0.255, 0.254, 0.557, 0.316, 0.307, 0.498, 0.517), (0.129, 0.044, 0.080, 0.148, 0.042, 0.079, 0.089, 0.099, 0.063, 0.144,0.075,0.163,0.001,0.144,0.099,0.051,0.215,0.089,0.132,0.133,0.114)
Double_Unit, Double_Unit_std = (0.383, 0.299, 0.296, 0.578, 0.215, 0.343, 0.547, 0.346, 0.436, 0.243, 0.395, 0.654, 0.381, 0.591, 0.361, 0.295, 0.321, 0.303), (0.085, 0.128, 0.087, 0.180, 0.053,0.117,0.131,0.055,0.142,0.092,0.118,0.100,0.239,0.009,0.117,0.093,0.053,0.066)
ALL_Unit, ALL_Unit_std = (0.307, 0.168, 0.188, 0.446, 0.184, 0.197,0.369, 0.245, 0.203, 0.394, 0.681,0.310, 0.305, 0.366, 0.255, 0.254, 0.557, 0.316, 0.307, 0.498, 0.517), (0.129, 0.044, 0.080, 0.148, 0.042, 0.079, 0.089, 0.099, 0.063, 0.144,0.075,0.163,0.001,0.144,0.099,0.051,0.215,0.089,0.009,0.133,0.114)

ind = np.arange(len(Single_Unit))
width = .75

fig, ax = plt.subplots()
rects1 = ax.bar((ind*3) - width, Single_Unit, width, yerr=Single_Unit_std,
                color='#6465A5', label='One Unit')
rects2 = ax.bar((ind*3), Double_Unit, width, yerr=Double_Unit_std,
                color='#F3E96B', label='Two Units')
rects3 = ax.bar((ind*3) + (width), ALL_Unit, width, yerr=ALL_Unit_std,
                color='#F05837', label='All repeats')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('TM score')
ax.set_title('TM score by repeats class and target length')
ax.set_xticks(ind*3)
ax.set_xticklabels(('II.2','III.1', 'III.2', 'III.3', 'III.4', 'III.5','IV.1', 'IV.2', 'IV.3', 'IV.4', 'IV.5','IV.6', 'IV.7', 'IV.8', 'IV.9', 'IV.10','V.1', 'V.2', 'V.3', 'IV.4', 'V.5',))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


#autolabel(rects1, "left")
#autolabel(rects2, "right")

plt.show()
