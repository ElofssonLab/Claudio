import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Initialize the figure with a logarithmic x axis
f, ax = plt.subplots(figsize=(7, 6))

# Load the example planets dataset
df =  pd.read_csv("table1.csv",header=0 )
print(df)
# Plot the orbital period with horizontal boxes
sns.boxplot(x="Pcons",data=df,
            whis=[0, 100], width=.6, palette="vlag")

# Add in points to show each observation
sns.stripplot(x="Pcons", data=df,
              size=4, color=".3", linewidth=0)

# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="")
sns.despine(trim=True, left=True)
plt.show() 

