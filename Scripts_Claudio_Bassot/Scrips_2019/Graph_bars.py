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

Single_Unit, Single_Unit_std = (0.167, 0.189, 0.185, 0.433, 0.197,0.362, 0.234, 0.203, 0.375, 0.681,0.311, 0.305, 0.363, 0.255, 0.557, 0.294, 0.287, 0.479, 0.530), (0.113, 0.157, 0.171, 0.152, 0.215, 0.095, 0.097, 0.038, 0.153, 0.075, 0.165, 0.001, 0.149, 0.102, 0.045, 0.090, 0.163, 0.157, 0.113)
Double_Unit, Double_Unit_std = (0.294, 0.298, 0.572, 0.228, 0.342,0.531, 0.417, 0.243, 0.389, 0.654,0.401, 0.591, 0.337, 0.308, 0.433, 0.306, 0.261, 0.283, 0.288), (0.127, 0.083, 0.183, 0.065, 0.108, 0.145, 0.140, 0.092, 0.125, 0.100, 0.249, 0.009, 0.098, 0.096, 0.194, 0.078, 0.140, 0.070, 0.067)
ALL_Unit, ALL_Unit_std = (0.369, 0.351, 0.419, 0.235, 0.339,0.641, 0.394, 0.294, 0.246, 0.508,0.324, 0.624, 0.249, 0.391, 0.330, 0.261, 0.282, 0.269, 0.242), (0.148, 0.110, 0.161, 0.046, 0.125, 0.139, 0.129, 0.176, 0.072, 0.036, 0.208, 0.101, 0.088, 0.165, 0.223, 0.049, 0.103, 0.038, 0.043)

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
ax.set_xticklabels(('III.1', 'III.2', 'III.3', 'III.4', 'III.5','IV.1', 'IV.2', 'IV.3', 'IV.4', 'IV.5','IV.6', 'IV.7', 'IV.8', 'IV.9','V.1', 'V.2', 'V.3', 'IV.4', 'V.5',))
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
