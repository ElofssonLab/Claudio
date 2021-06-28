import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('benchmark.csv',header = None, names=['ID','TMscore','Pcons'])

# Fixing random state for reproducibility

x = df['Pcons']
y = df['TMscore']
z=df['ID']
print(z)
fig, ax = plt.subplots()
ax.fmt_ydata = df
plt.plot(x, y, 'o')
ax.set(xlim=(0,1))
ax.set_ylabel('TMscore')
ax.set_xlabel('Pcons')
for i, txt in enumerate(z):
    ax.annotate(z[i], (x[i], y[i]))

plt.show()


