#!/bin/bash

# For loop over all model conditions and replicates
csv="/mnt/c/Users/joy/Desktop/svd/files/data-species-tree.csv";

indel="/mnt/c/Users/joy/Desktop/svd/result/data/"
noindel="/mnt/c/Users/joy/Desktop/svd/noindel/data"
paths=( "$indel" "$noindel")
for path in "${paths[@]}"; do
  if [ "$path" == "$indel" ]; then
	label="indel"
  
  elif [ "$path" == "$noindel" ]; then 
	label="noindel"
  fi
  echo "$path"
  for taxa in 25 10 50; do
    for rate in 10000000 5000000 1000000 500000 100000; do
        modl="simphy-${taxa}tax-1000gen-${rate}su"
	echo "$modl"
        for repl in `seq -f "%02g" 1 15`; do
        echo "$repl" 
        if [ -e "/mnt/c/Users/joy/Desktop/svd/files/${modl}-${label}-svd-${repl}-paup.tre" ]; then
           continue;
        fi
        list=()
        for gene in `seq -f "%04g" 1 1000`; do
            list=( ${list[@]} "${path}/${modl}/$repl/g_trees${gene}_TRUE.phy" )
        done
        #echo ${list[@]}
        python d_run_svdquartets_2.py -i ${list[@]} \
                              -c "/mnt/c/Users/joy/Desktop/svd/files/${modl}-${label}-cat-${repl}" \
                              -o "/mnt/c/Users/joy/Desktop/svd/files/${modl}-${label}-svd-${repl}" 
        python extract_quartets_from_paup.py \
            "/mnt/c/Users/joy/Desktop/svd/files/${modl}-${label}-svd-${repl}.log"\
            "/mnt/c/Users/joy/Desktop/svd/files/${modl}-${label}-svd-${repl}-weighted-quartets.txt"

        sed 's/_0_0//g' "/mnt/c/Users/joy/Desktop/svd/files/${modl}-${label}-svd-${repl}-paup.tre" > "/mnt/c/Users/joy/Desktop/svd/files/${modl}-${label}-svd-${repl}-paup-renamed.tre"

        xxx=$(term=ANSI python compare_trees.py \
              "/mnt/c/Users/joy/Desktop/svd/data/${modl}/$repl/s_tree.trees" \
              "/mnt/c/Users/joy/Desktop/svd/files/${modl}-${label}-svd-$repl-paup-renamed.tre")
              
        echo "$label,$taxa,$rate,$repl,${xxx[@]}" >> $csv

#./max-cut-tree \
#   qrtt="../simphy-10tax-1000gen-500000su/svd-${repl}-weighted-quartets.txt" \
#   otre="../simphy-10tax-1000gen-500000su/svd-${repl}-wqmc.tre"

#./max-cut-tree \
#   qrtt="../simphy-10tax-1000gen-500000su/svd-${repl}-quartets.txt" \
#   otre="../simphy-10tax-1000gen-500000su/svd-${repl}-qmc.tre"
            done
        done
    done
done
