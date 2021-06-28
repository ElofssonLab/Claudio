import re
import linecache

#h = sys.argv[1]
f = open("hhpred_5a1s_cons1.hhr", "r")

print f

tot_lines = len(f.readlines())

line1 = list(linecache.getline("hhpred_5a1s_cons1.hhr",22))
line2 = list(linecache.getline("hhpred_5a1s_cons1.hhr",32))
line3 = list(linecache.getline("hhpred_5a1s_cons1.hhr",42))
line4 = list(linecache.getline("hhpred_5a1s_cons1.hhr",52))
line5 = list(linecache.getline("hhpred_5a1s_cons1.hhr",62))

TM_score=""

for i in range(23,102):
    TM_score+= str(line1[i])
    TM_score+= str(line2[i])
    TM_score+= str(line3[i])
    TM_score+= str(line4[i])
for i in range(23,58):
    TM_score+= str(line5[i])

print TM_score
