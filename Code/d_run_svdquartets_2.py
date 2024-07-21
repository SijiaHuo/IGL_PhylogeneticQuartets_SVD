"""
Script concatenates gene alignments and runs SVDQuartets.

Authors: Wendi Chen, Sijia Huo, Pengzheng Zhang, Rex Zhou
Advisors: Erin Molloy* (emolloy2@illinois.edu),
          Ruth Davidson (redavids2@illinois.edu)
* indicates primary author
"""
import argparse
import alignment
import os
import sys
import shutil

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
    with open(qfile, 'r') as f:
        filetext = f.read().split('\n') # MAY NEED: \r\n

    # Change "1  2 |  3  4   7.2980e-05" into
    # q = "1,2|3,4:0.000072980"

    # Returning weighted quartets as list
    start_read = False

    print filetext[0]

    for line in filetext:
        print line
        sys.exit()
        if '|' in line:
            start_read = True
        if start_read:
            if line in ['\n', '\r\n']:
                break
            quartets.append(weighted_quartets_paup_line_parse(line))
        print quartets
	return quartets

def concatenate(files,num):
    c = []
    for f in files:
        c.append(alignment.read_phylip(f,num))
    a = alignment.concatenate(c)
    return a

def main(args):
    # Create/write concatenated alignment
    if args.concatenated is None:
        cfile = "concatenated.nex"
    else:
        cfile = args.concatenated + ".nex"
    a = concatenate(args.input,args.num_sites)
    a.write_nexus(cfile)
    # Run SVDQuartets
    if args.output is None:
        oname = "output"
    else:
        oname = args.output

    qfile = 'tmp-' + "quartets.txt"
    pfile = 'tmp-' + "paup.tre"
    cmd = "echo \"exe " + cfile + "; svd showScores=yes forceRank=10 evalQuartets=all treeInf=QFM qfile=" + qfile + " qformat=qmc; savetrees file=" + pfile + " format=newick;\" | ./paup4a157_centos64 -n"
    #os.system(cmd)
    out = os.popen(cmd).read()
    with open(oname + '.log', 'w') as f:
        f.write(out)

    shutil.move(qfile, oname + '-quartets.txt')
    shutil.move(pfile, oname + '-paup.tre')

    #wq = weighted_quartets_from_paup(oname + '.log')
    #with open(oname + '-weighted-quartets.txt', 'w') as f:
    #    f.write(' '.join(wq))
    
    #sys.exit()
    # Run QMC --- @ZPZ IS GOING TO FIX THIS!
    #tfile = r + "-qmc.tre"
    #cmd = "./max-cut-tree qrtt=" + qfile + " otre=" + tfile
    #os.system(cmd)

    # Move files
    #cmd = "mv " + r + "-* " + path
    #os.system(cmd)


if __name__ == "__main__":
   parser = argparse.ArgumentParser()

   parser.add_argument("-i", "--input", type=str, nargs='+',
                        help='Input alignment file(s).', required=True)

   parser.add_argument("-c", "--concatenated", type=str,
                       help="Name of output concatenated alignment.")

   parser.add_argument("-o", "--output", type=str,
                       help="Prefix of output for SVDquartets.")
   parser.add_argument("-n","--num_sites",type=int,
			help="num of sites to extract.")
   main(parser.parse_args())
