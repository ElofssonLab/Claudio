#!/bin/env python

import sys
import argparse
import gaussdca

MSA = sys.argv[1]
results = gaussdca.run(MSA)                             
results.keys()

print(MSA, results['eff_seq'])
