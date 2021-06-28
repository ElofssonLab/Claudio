import matplotlib.pyplot as plt

# Pie chart
plt.rcParams['font.size'] = 18
labels = ['Bacteria','Eukaryota', 'Bacteria and Eukaryota', ]
sizes = [20, 33, 138]# only "explode" the 2nd slice (i.e. 'Hogs')
explode = (0, 0.1, 0)
fig1, ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)# Equal aspect ratio ensures that pie is drawn as a circle

ax1.axis('equal') 
plt.tight_layout()


plt.show()
