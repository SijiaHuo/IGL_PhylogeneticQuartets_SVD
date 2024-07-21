#!/bin/bash

# For loop over all model conditions and replicates
storage="/mnt/c/Users/joy/Desktop/svd/sites_files"
csv="${storage}/data-species-tree.csv";
#echo "SITE,LABEL,TAXA,RATE,REPL,NL,E1,E2,FP,FN,RF">$csv #comment this line if you run the code mutiple times to finish a single round.
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
for site in 1 10 100; do
  for taxa in 25 10 50; do
    for rate in 10000000 5000000 1000000 500000 100000; do
        modl="simphy-${taxa}tax-1000gen-${rate}su"
	echo "$modl"
        for repl in `seq -f "%02g" 1 15`; do
            echo "$repl" 
            if [ ! -e "${storage}/${modl}-${label}-svd-${site}sites-${repl}-paup.tre" ]; then
                list=()
                for gene in `seq -f "%04g" 1 1000`; do
                    list=( ${list[@]} "${path}/${modl}/$repl/g_trees${gene}_TRUE.phy" )
                done
                #echo ${list[@]}
                python d_run_svdquartets_2.py -i ${list[@]} \
                                              -c "${storage}/${modl}-${label}-cat-${site}sites-${repl}" \
                                              -o "${storage}/${modl}-${label}-svd-${site}sites-${repl}" \
			                      -n ${site}
                python extract_quartets_from_paup.py \
                    "${storage}/${modl}-${label}-svd-${site}sites-${repl}.log"\
                    "${storage}/${modl}-${label}-svd-${site}sites-${repl}-weighted-quartets.txt"
        
	        sed 's/_0_0//g' "${storage}/${modl}-${label}-svd-${site}sites-${repl}-paup.tre" > "${storage}/${modl}-${label}-svd-${site}sites-${repl}-paup-renamed.tre"
	    fi
	    
	    if [ ! -e "${storage}/${modl}-${label}-svd-${site}sites-${repl}-paup.tre" ]; then
	        echo "Unable to make ${storage}/${modl}-${label}-svd-${site}sites-${repl}-paup.tre!!"
	    fi
	
            #xxx=$(term=ANSI python compare_trees.py \
            #    "/mnt/c/Users/joy/Desktop/svd/data/${modl}/$repl/s_tree.trees" \
            #    "${storage}/${modl}-${label}-svd-${site}sites-$repl-paup-renamed.tre")
              
            #echo "$site,$label,$taxa,$rate,$repl,${xxx[@]}" >> $csv
                done
            done
        done
    done
done
