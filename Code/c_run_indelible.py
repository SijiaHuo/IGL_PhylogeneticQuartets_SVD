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

indelible = "./indelible-1.03-lnx64"
# indelible = "./indelible-1.03-osx_intel"
# indelible = "./indelible-1.03-windows.exe"


def generate_control(trefile, outname):
    with open(trefile, 'r') as f:
        tree = f.read()

    with open("control.txt", "w") as f:
        f.write("[TYPE] NUCLEOTIDE 1\n")
        f.write("[MODEL]    modelname\n")
        f.write("[submodel]     JC\n")
        f.write("[TREE] treename  " + tree + "\n")
        f.write("[PARTITIONS] partitionname\n")
        f.write("  [treename modelname 1000]\n")
        f.write("[EVOLVE] partitionname 1 " + outname + "\n")


if __name__ == "__main__":
    ngen = [50, 1000]
    pads = [2, 4]
    mods = ["simphy-5tax-50gen-1000bps/",
            "simphy-5tax-1000gen-50bps/"]

    nrep = 10
    reps = [str(r).zfill(2) for r in range(1, nrep + 1)]

    for mo, ng, pa in zip(mods, ngen, pads):
        gs = [str(g).zfill(pa) for g in range(1, ng+1)]
        for r in reps:
            path = "../data/" + mo + r + "/"
            for g in gs:
                name = "true-gene-" + g

                trefile = path + name + ".tre"
                generate_control(trefile, name)
                subprocess.call([indelible])
                os.rename("LOG.txt",
                          path + "indelible-gene-" + g + ".log")
                os.rename(name + ".fas", path + name + ".fas")
                os.rename(name + "_TRUE.phy", path + name + "_TRUE.phy")
