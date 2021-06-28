import string
import sys
import argparse



chains = list(string.ascii_uppercase)
chains.extend(list(string.ascii_lowercase))

known_res = {"ALA","CYS","ASP","GLU","PHE","GLY",
			"HIS","HID","HIE","HIP","HSP","HSE","HSP","HSD",
			"ILE","LYS","LEU","MET","ASN","PRO","GLN","ARG",
			"SER","THR","VAL","TRP","TYR","TYR"}




def change_chain_name(inputfile, outfile = None, breakLen = 2, keepHet = True, keepWater = False):

	new_ch = 0 
	old_pos = None

	chain_size = 0

	res_id_dict = {}

	if outfile:
		fout = open(outfile, "w")
	
	with open(inputfile) as f:
		for line in f:
			if line:
				if line.startswith("ATOM"):
					left = line[0:21]
					middle = line[21:27]
					rigth = line[27:-1]
					
					
					ch = middle[0]
					pos = int(middle[1:])
					
					res = line[17:20]
					res_num = int(middle[1:])
					atom = left[11:17]
					
					
					if res not in known_res:
						left = "HETATM" + left[6:]
						
						
					'''
					print "->{}<-".format(left)
					print "->{}<-".format(middle)
					print "->{}<-".format(rigth)
					print line
					'''
					'''
					->HETATM
					->ATOM     11  CA  LYS <-
					->P   2 <-
					->    -21.501 101.030  60.308  1.00  0.00<-
					ATOM     11  CA  LYS P   2     -21.501 101.030  60.308  1.00  0.00
					'''
					
					if old_pos and abs(old_pos-pos) >= breakLen:
						new_ch += 1
						
						if chain_size > 1:
							if outfile:
								fout.write("TER\n")
							else:
								print "TER", chain_size
						
						chain_size = 0
						
					if res in known_res or keepHet:
						if res != "TIP" or keepWater:
							
							chain_size += 1
							
							#	Increase residue number if already used
							res_num_new = increase_pos(res_id_dict, chains[new_ch], res, res_num, atom)							
							
							
							
							if outfile:
								fout.write("{}{}{}{}\n".format(left,chains[new_ch],res_num_new,rigth))
							else:
								print "{}{}{}{}".format(left,chains[new_ch],res_num_new,rigth)
							
					old_pos = pos
					
				else:
					if outfile:
						fout.write(line)
					else:
						print line[:-1]
					
	return

def increase_pos(res_id_dict, new_ch, res, res_num, atom):
	res_id = "#".join([new_ch,res,str(res_num),atom]) 
	if res_id not in res_id_dict:
		res_id_dict[res_id] = None
		return "{:>4.4} ".format(str(res_num))
	else:
		return increase_pos(res_id_dict, new_ch, res, res_num + 1, atom)

####################################################


'''
Command line arguments parser
'''
def argParser():
	
	parser = argparse.ArgumentParser(prog='add_chains.py',description="Add chain names for artificial PDBs created for MD symulations",
					formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	
	parser.add_argument('pdbFile',
						help='PDB input file.')
	
	parser.add_argument('-o','--outFile',default=None,
						help='Output file name')
	
	parser.add_argument('-b','--breakLen',default=2, type=int,
						help='Allowed chain-break length before chanching chain name')					
	
	parser.add_argument('-k','--keepHet',action='store_false',default=True,
						help='Keep hetero atoms')
	parser.add_argument('-w','--keepWater',action='store_true',default=False,
						help='Keep water molecules (TESTING)')
	parser.add_argument('-v','--verbose',action='store_true',default=False)
						
	# Initialize the parser object
	args=parser.parse_args()

	return args

##################################################

	
args = argParser()

change_chain_name(args.pdbFile, outfile = args.outFile, breakLen = args.breakLen, keepHet = args.keepHet, keepWater = args.keepWater)

# ls old_pdbs/ | while read line; do python add_chains.py old_pdbs/$line -o new_pdbs/$line -b 20; done
	
