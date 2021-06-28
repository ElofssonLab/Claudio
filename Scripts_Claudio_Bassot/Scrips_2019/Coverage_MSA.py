from __future__ import division
import sys
import linecache

# filename and number of lines requested
fname = sys.argv[1]
#out= sys.argv[2]

# count the total number of lines
tot_lines = int((len(open(fname).readlines()))/2)
lines = []
R_list = []
lines = [i for i in range(0, tot_lines+1) if i  != 0]
for i in lines:
    m = i*2
    #print int(m)
    line = list(linecache.getline(sys.argv[1], m))
    len_seq =len(line)
    #print line
    seq = [item for item,x in enumerate(line)]
    # print seq
    gap = 0    
    counter = 0 
    for l in seq:
          if line[l] == "-":
            gap += 1 
            #print gap
    R = float(gap/len_seq)
    R_list.append(R)

for r in R_list:
    if r < 0.25:
        counter += 1
        continue
       
    else: 
        continue
        
#print counter
coverage = counter/tot_lines

print fname, coverage
