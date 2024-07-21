#!/bin/bash

# For loop over all model conditions and replicates
storage="/mnt/c/Users/joy/Desktop/svd/mixed_rates_files"
csv="${storage}/data-mixe-tree.csv";
echo "SITE,LABEL,TAXA,RATE,REPL,NL,E1,E2,FP,FN,RF">$csv #comment this line if you run the code mutiple times to finish a single round.
indel="/mnt/c/Users/joy/Desktop/svd/result/data"
noindel="/mnt/c/Users/joy/Desktop/svd/noindel/data"
paths=( "$indel" "$noindel")


for path in "${paths[@]}"; do
  if [ "$path" == "$indel" ]; then
	label="indel"
  
  elif [ "$path" == "$noindel" ]; then 
	label="noindel"
  fi
  echo "$path"
for site in 100; do
  for taxa in 25 10 50; do
    for repl in `seq -f "%02g" 1 15`; do
      echo "$repl"
      for rate in "uniform" "biased"; do
        modl="simphy-${taxa}tax-1000gen-${rate}rate"
        if [ -e "${storage}/${modl}-${label}-svd-${site}sites-${repl}-paup.tre" ]; then
	   echo "processed {$modl}!"
           continue;
        fi
	list=()
	if [ $rate == "uniform" ]; then
            for g in `seq 1 1000`; do
	        gene=$(printf "%04g" $g)
		# 10000000 5000000 1000000 500000 100000
	        if [ $g -le 200 ]; then
		    modl="simphy-${taxa}tax-1000gen-10000000su"
		elif [ $g -ge 201 ] && [ $g -le 400 ]; then
		    modl="simphy-${taxa}tax-1000gen-5000000su"
		elif [ $g -ge 401 ] && [ $g -le 600 ]; then
		    modl="simphy-${taxa}tax-1000gen-1000000su"
		elif [ $g -ge 601 ] && [ $g -le 800 ]; then
		    modl="simphy-${taxa}tax-1000gen-500000su"
		else
		    modl="simphy-${taxa}tax-1000gen-100000su"
		fi
                list=( ${list[@]} "${path}/${modl}/$repl/g_trees${gene}_TRUE.phy" )
            done
	else
	    for g in `seq 1 1000`; do
	        gene=$(printf "%04g" $g)
		# 10000000 5000000 1000000 500000 100000
	        if [ $g -le 350 ]; then
		    modl="simphy-${taxa}tax-1000gen-100000su"
		elif [ $g -ge 351 ] && [ $g -le 700 ]; then
		    modl="simphy-${taxa}tax-1000gen-500000su"
		elif [ $g -ge 701 ] && [ $g -le 800 ]; then
		    modl="simphy-${taxa}tax-1000gen-1000000su"
		elif [ $g -ge 801 ] && [ $g -le 900 ]; then
		    modl="simphy-${taxa}tax-1000gen-5000000su"
		else
		    modl="simphy-${taxa}tax-1000gen-10000000su"
		fi
                list=( ${list[@]} "${path}/${modl}/$repl/g_trees${gene}_TRUE.phy" )
            done
	fi
#        echo ${list[@]}
	modl="simpyh-${taxa}tax-1000gen-${rate}_rate"
        python d_run_svdquartets_2.py -i ${list[@]} \
                              -c "${storage}/${modl}-${label}-cat-${site}sites-${repl}" \
                              -o "${storage}/${modl}-${label}-svd-${site}sites-${repl}" \
			      -n ${site}
        python extract_quartets_from_paup.py \
            "${storage}/${modl}-${label}-svd-${site}sites-${repl}.log"\
            "${storage}/${modl}-${label}-svd-${site}sites-${repl}-weighted-quartets.txt"

        sed 's/_0_0//g' "${storage}/${modl}-${label}-svd-${site}sites-${repl}-paup.tre" > "${storage}/${modl}-${label}-svd-${site}sites-${repl}-paup-renamed.tre" 
        s_tree="simphy-${taxa}tax-1000gen-10000000su"
        xxx=$(term=ANSI python compare_trees.py \
              "/mnt/c/Users/joy/Desktop/svd/data/${s_tree}/$repl/s_tree.trees" \
              "${storage}/${modl}-${label}-svd-${site}sites-$repl-paup-renamed.tre")
              
        echo "$site,$label,$taxa,$rate,$repl,${xxx[@]}" >> $csv
                done
            done
        done
    done
done
