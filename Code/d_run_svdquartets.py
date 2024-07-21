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

def concatenate(files):
    c = []
    for f in files:
        c.append(alignment.read_phylip(f))
    a = alignment.concatenate(c)
    return a

def main(args):
    # Create/write concatenated alignment
    if args.concatenated is None:
        cfile = "concatenated.nex"
    else:
        cfile = args.concatenated + ".nex"
    a = concatenate(args.input[:3])
    a.write_nexus(cfile)

    # Run SVDQuartets
    if args.output is None:
        oname = "output"
    else:
        oname = args.output

    qfile = 'tmp-' + "quartets.txt"
    wfile = 'tmp-' + "weighted-quartets.txt"
    pfile = 'tmp-' + "paup.tre"
    xfile = 'tmp-' + "paup-test.tre"
    cmd = "echo \"exe " + cfile + "; svd showScores=yes forceRank=10 evalQuartets=all treeInf=QFM qfile=" + qfile + " qformat=qmc; savetrees file=" + pfile + " format=newick;\" | ./paup4a157_centos64 -n"
    #os.system(cmd)
    out = os.popen(cmd).read()
    with open(oname + '.log', 'w') as f:
        f.write(out)
    
    os.rename(qfile, oname + 'quartets.txt')
    sys.exit()

    # Run QMC 
    tfile = r + "-qmc.tre"
    cmd = "./max-cut-tree qrtt=" + qfile + " otre=" + tfile
    os.system(cmd)

    # Move files
    cmd = "mv " + r + "-* " + path
    os.system(cmd)


if __name__ == "__main__":
<<<<<<< HEAD
   parser = argparse.ArgumentParser()

   parser.add_argument("-i", "--input", type=str, nargs='+',
                        help='Input alignment file(s).', required=True)

   parser.add_argument("-c", "--concatenated", type=str,
                       help="Name of output concatenated alignment.")

   parser.add_argument("-o", "--output", type=str,
                       help="Prefix of output for SVDquartets.")
=======
    ngen = [1000]
    pads = [4]
    mods = ["simphy-10tax-1000gen-100000su"]

    nrep = 10
    reps = [str(r).zfill(2) for r in range(1, nrep + 1)]

    for mo, ng, pa in zip(mods, ngen, pads):
        gs = [str(g).zfill(pa) for g in range(1, ng+1)]
        for r in reps:
            path = "/mnt/c/Users/joy/Desktop/svd/noindel/data/" + mo

            # Concatenate gene alignments
            cfile = r + "-concatenated.nex"
            afiles = []
            for g in gs:
                afiles.append(path + "/" + r + "/" + "g_trees" + g + ".fas")
            a = concatenate(afiles)
            a.write_nexus(cfile)

            # Run SVDQuartets
            qfile = r + "-quartets.txt"
            pfile = r + "-paup.tre"
            cmd = "echo \"exe " + cfile + "; svd showScores=yes forceRank=10 evalQuartets=all treeInf=qfm qfile=" + qfile + " qformat=qmc ; savetrees file=" + pfile + " format=newick;\" | ./paup4a157_centos64 -n"
            os.system(cmd)

#	    os.system("python extract_quartets_from_paup.py "+qfile+" "+ qfile+"-with_score")

            # Run QMC 
            tfile = r + "-qmc.tre"
            cmd = "./max-cut-tree qrtt=" + qfile + " otre=" + tfile
            os.system(cmd)

            # Move files
            cmd = "mv " + r + "-* " + path
            os.system(cmd)
>>>>>>> 1c97b498838cd7624dab9ba83dc19de5c95da54c

   main(parser.parse_args())
