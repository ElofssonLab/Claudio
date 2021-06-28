import pandas as pd
import sys
import csv
import argparse
from collections import Counter

out = sys.argv[1]

df =  pd.read_csv("architecture2.txt", sep='\t',)
list_ID = open("ID_no_PDB", 'r')
df1 =  pd.read_csv("ID_no_PDB", sep='\t',)
 
#mykewords = df1["ID"]
#for index, row in df.iterrows():
#    print df['Domains'].value_counts()

mydic = {}
mydict = dict(zip(df.n, df.Domains))

print mydict
def freq(str): 
  
    # break the string into list of words 
    str_list = str.split() 
  
    # gives set of unique words 
    unique_words = set(str_list) 
      
    for words in unique_words : 
        print(words , str_list.count(words)) 
  
# driver code 
if __name__ == "__main__": 
    for domains in mydict.values():  
            freq(domains) 

