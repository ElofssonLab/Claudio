# Standard library packages
import io
import linecache
# Import Seaborn for graphics and plotting
import seaborn as sns

# Import bioservices module, to run remote UniProt queries
from bioservices import UniProt

# Import Pandas, so we can use dataframes
import pandas as pd
# Import sys
import sys 
query = sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]
output = sys.argv[4]
# Make a link to the UniProt webservice
service = UniProt()

# Build a query string

# Send the query to UniProt, and catch the search result in a variable
result = service.search(query, frmt="fasta")

# Inspect the result
#print(result)
fasta = str(result)
seq = fasta.split("\n",1)[1];
header = fasta.split("\n",1)[0]
#print header
#seq )

seq =seq.replace("\n","")
unit = seq[int(start)-1 :int(end)]

print unit
with open(output, "w") as g:
    g.write(header+"\n"+ unit) 
    g.close
