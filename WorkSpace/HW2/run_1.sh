#!/bin/bash

if [[ $# -ne 1 ]] ; then
    echo "usage: ./matrix_multiply_parallel num_threads"
    exit 1
fi
export OMP_NUM_THREADS=$1

#alias time='/usr/bin/time'
#time --output=time_stats_run1.txt -a ./matrix_multiply_parallel 2000_2000_int_matrix.dat 2000

#echo "Removing Previous time_stats_run1.txt"
#rm time_stats_run.txt

'/usr/bin/time' -o time_stats_run1.txt -a -f '%e %U %S' ./matrix_multiply_parallel 2000_2000_int_matrix.dat 2000

'/usr/bin/time' -o time_stats_run1.txt -a -f '%e %U %S' ./matrix_multiply_parallel 4000_4000_int_matrix.dat 4000

'/usr/bin/time' -o time_stats_run1.txt -a -f '%e %U %S' ./matrix_multiply_parallel 8000_8000_int_matrix.dat 8000

#'/usr/bin/time' -o time_stats_run1.txt -a -f '%e %U %S' ./matrix_multiply_parallel 10_10_int_matrix.dat 10

#'/usr/bin/time' -o time_stats_run1.txt -a -f '%e %U %S' ./matrix_multiply_parallel 25_25_int_matrix.dat 25

#'/usr/bin/time' -o time_stats_run1.txt -a -f '%e %U %S' ./matrix_multiply_parallel 50_50_int_matrix.dat 50


