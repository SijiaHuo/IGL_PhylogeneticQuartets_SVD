#!/bin/bash
# Script for creating datasets with species and gene trees.
# 
# Basic command comes from 
# https://github.com/redavids/HGT-Simulations/blob/master/simPhySimulation.sh
#
# Simpy Options:
# -rs : Number of species tree replicates
# -rl : Number of locus trees per species tree
# -rg : Number of gene trees per locus tree
# -st : Species tree height (time units)
# -si : Number of individuals per species
# -sl : Number of taxa (leaves)
# -sb : Speciation rate (events/time unit)
# -cp -> sp: Tree­wide effective population size
# -hs : Species­specific branch rate heterogeneity modifiers
# -hl : Gene­-family-­specific rate heterogeneity modifiers
# -hg : Gene­-by-­lineage­-specific rate heterogeneity modifiers
# -cu -> su : Tree­wide substitution rate
# -so : Ratio between ingroup height and the branch from the root to the ingroup.
#       If this parameter is not set the outgroup is not simulated.
# -od : Activates the SQLite database output.
# -v : Verbosity
# -cs : Random number generator seed.
# -o : Common output prefix­name (for folders and files).

# Undergraduate Student Authors: Wendi Chen, Sijia Huo, Pengzheng Zhang, Rex Zhou
# Graduate Student Authors: Erin Molloy
# Advisors: Erin Molloy (emolloy2@illinois.edu),
#           Ruth Davidson (redavids2@illinois.edu)
# -------------------------------------------------------------------------------
SIMPHY="./simphy-1.0.2-lnx64"
#SIMPHY="./simphy-1.0.2-mac64"


nr=10
ngs=( 50 1000 )
nbs=( 1000 50 )

# Generage data
for i in `seq 0`; do
    ng=${ngs[$i]}
    nb=${nbs[$i]}

    # Original
    $SIMPHY -rs $nr \
            -rl F:$ng \
            -rg 1 \
            -si F:1 \
            -sl F:6 \
            -sb F:0.000001 \
            -sp F:2000000 \
            -v 6  \
            -o simphy-6tax-${ng}gen-${nb}bps \
            | tee simphy-6tax-${ng}gen-${nb}bps.log

    # From Ruth
    $SIMPHY -rs $nr \
            -rl F:$ng \
            -rg 1 \
            -st F:2000000 \
            -si F:1 \
            -sl F:5 \
            -sb F:0.000001 \
            -sp F:200000 \
            -hs LN:1.5,1 \
            -hl LN:1.2,1 \
            -hg LN:1.4,1 \
            -su E:10000000 \
            -so F:1 \
            -od 1 \
            -v 3  \
            -cs 293745 \
            -o simphy-5tax-${ng}gen-${nb}bps \
            | tee simphy-5tax-${ng}gen-${nb}bps.log
done

mv simphy-6tax-* ../data
mv simphy-5tax-* ../data
