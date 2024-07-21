d_run.sh: run svdquartets on all the conditions
d_run.sh: run svdquartets on 1 10 100 long sites
d_run_mixed_rates.sh: run svdquatets on mixed substitution rates
To use:
  1.Make sure you have the .sh files and the d_run_svdquartets_2.py, alignment.py and paup4a157_centos64 under same directory.
  2.Change the storage variable inside the .sh files in paths where you want to store your results.
  3.Change s_trees noindel indel and cvs variables into your local path accordingly.
  4.You can interrupt the process and rerun it from where you stopped. If you want to do so, please make sure to comment out the line of echo "blah blah ...">$csv or else it will insert the lables mutiple times.
