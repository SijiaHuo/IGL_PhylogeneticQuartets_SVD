"""
Script runs INDELible on each gene tree.
Authors: Wendi Chen*, Sijia Huo, Pengzheng Zhang, Rex Zhou
Advisors: Erin Molloy (emolloy2@illinois.edu),
          Ruth Davidson (redavids2@illinois.edu)
* indicates primary author
"""
import subprocess
import shutil
import os
import sys

#indelible = "./indelible-1.03-lnx64"
# indelible = "./indelible-1.03-osx_intel"
indelible = "./indelible-1.03-windows.exe"


def generate_control(trefile, outname):
    with open(trefile, 'r') as f:
        tree = f.read()

    with open("control.txt", "w") as f:
        f.write("[TYPE] NUCLEOTIDE 1\n")
        f.write("[MODEL]    modelname\n")
        f.write("[submodel]  GTR 1.2619573850882344 0.14005536945585983 0.2877830346145434 0.35766826674033914 0.3082674310184066\n")
        f.write("[statefreq]  .311475 .191363 .300414 .196748\n")
        f.write("[rates]     0 1 0 \n")
        f.write("[indelmodel]   POW  1.7 500\n")
        f.write("[indelrate]    0.0001\n")
        f.write("[TREE] treename  " + tree + "\n")
        f.write("[PARTITIONS] partitionname\n")
        f.write("  [treename modelname 1000]\n")
        f.write("[EVOLVE] partitionname 1 " + outname + "\n")


if __name__ == "__main__":
    ngen = [1000]
    pads = [4]
    mods = ["simphy-10tax-1000gen-100000su/","simphy-10tax-1000gen-500000su/","simphy-10tax-1000gen-1000000su/","simphy-10tax-1000gen-5000000su/","simphy-10tax-1000gen-10000000su/",
            "simphy-25tax-1000gen-100000su/","simphy-25tax-1000gen-500000su/","simphy-25tax-1000gen-1000000su/","simphy-25tax-1000gen-5000000su/","simphy-25tax-1000gen-10000000su/",
            "simphy-50tax-1000gen-100000su/","simphy-50tax-1000gen-500000su/","simphy-50tax-1000gen-1000000su/","simphy-50tax-1000gen-5000000su/","simphy-50tax-1000gen-10000000su/"
            ]

    nrep = 15
    reps = [str(r).zfill(2) for r in range(1, nrep + 1)]

    for mo in mods:
        ng=1000
        pa=4
        gs = [str(g).zfill(pa) for g in range(1, ng+1)]
        for r in reps:
            path = "data/" + mo + r + "/"
            for g in gs:
                name = "g_trees" + g

                trefile = path + name + ".trees"
                generate_control(trefile, name)
                subprocess.call([indelible])
                if not os.path.exists("result/"+path):
                    os.makedirs("result/"+path)
                os.rename("LOG.txt",
                          "result/"+path + "indelible-gene-" + g + ".log")
                os.rename(name + ".fas", "result/"+path + name + ".fas")
                os.rename(name + "_TRUE.phy","result/"+ path + name + "_TRUE.phy")
