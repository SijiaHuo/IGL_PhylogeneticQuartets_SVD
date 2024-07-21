import sys

def weighted_quartets_paup_line_parse(line):
	"""
	Parameters
	----------
	line : a line from the paup output that needs to be formatted
	
	Returns
	-------
	out_line : a line in the format 1,2|3,4:weight

	"""
	# splitting the line up into elements 
	x = line.split()

	# merging with the correct formatting
	if len(x) == 7:
		out_line = x[1] + "," + x[2] + x[3] + x[4] + "," + x[5] + ":" + str("%1.12f" % float(x[6]))
	else:
		out_line = x[0] + "," + x[1] + x[2] + x[3] + "," + x[4] + ":" + str("%1.12f" % float(x[5]))
	
	# returning the correct string
	return out_line

def weighted_quartets_from_paup(qfile):
	"""
	Parameters
	----------
	qfile : a text file with the output from paup

	Returns
	-------
	quartets : a list of strings in the form 1,2|3,4:weight

	"""
	# setting up the list
	quartets = []
	
	# Opening and setting up text input
	inputfile = open(qfile)
	filetext = inputfile.readlines()

	# Change "1  2 |  3  4   7.2980e-05" into
    # q = "1,2|3,4:0.000072980"

	# Returning weighted quartets as list
	start_read = False

	for line in filetext:
		if '|' in line:
			start_read = True
		if start_read :
			if line in ['\n', '\r\n']:
				break
			quartets.append(weighted_quartets_paup_line_parse(line))
		
	return quartets

if __name__ == "__main__":
    argc = len(sys.argv)
    assert (argc == 3), \
    "Usage: extract_quartets_from_paup.py infile outfile"

    ifile = str(sys.argv[1])
    ofile = str(sys.argv[2])

    quartets = weighted_quartets_from_paup(ifile)

    with open(ofile, 'w') as f:
        f.write(' '.join(quartets))
