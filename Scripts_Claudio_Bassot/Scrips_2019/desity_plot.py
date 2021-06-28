import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Import Data
df = pd.read_csv("all_contact_type2")

# Draw Plot
plt.figure(figsize=(13,10), dpi= 80)
sns.distplot(df.loc[df['Type'] == 'Contact', "score"], color="dodgerblue", label="Contact", hist_kws={'alpha':.5}, kde_kws={'linewidth':3})
sns.distplot(df.loc[df['Type'] == 'Conf_Contact', "score"], color="orange", label="Conf_Contact", hist_kws={'alpha':.5}, kde_kws={'linewidth':3})
sns.distplot(df.loc[df['Type'] == 'No_contact', "score"], color="r", label="No_contact", hist_kws={'alpha':.5}, kde_kws={'linewidth':3})
plt.ylim(0, 10)

# Decoration
plt.title('Contacs', fontsize=22)
plt.legend()
plt.show()

