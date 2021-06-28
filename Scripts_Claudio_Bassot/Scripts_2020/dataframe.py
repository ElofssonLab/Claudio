from __future__ import division
import pandas as pd
import glob
import numpy as np


path = '.'
all_files = glob.glob(path + "/*.intra_DMP_ppv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=None, error_bad_lines=False, sep = ' ')
    df.columns = ['res1', 'res2', 'score', 'dist']
   # print df
    cont = np.sum(df['dist'] <= 8.0)
    df1 = df.head(cont)
    L_cont = np.sum(df1['dist'] <= 8.0)
    PPV = L_cont/cont
    df2 = (filename, PPV, L_cont, cont)

    print df2
  
#    li.append(df)

#frame = pd.concat(li, axis=0, ignore_index=True)
