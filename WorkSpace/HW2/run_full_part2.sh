#!/bin/bash

if [[ $# -ne 0 ]] ; then
    echo "usage: Dont do anything.. just run the thing and let it run the others. Boom."
    exit 1
fi
#export OMP_NUM_THREADS=$1
#alias time='/usr/bin/time'
#time --output=time_stats_run1.txt -a ./matrix_multiply_parallel 2000_2000_int_matrix.dat 2000
#echo "Removing Previous time_stats_run1.txt"
#rm time_stats_run.txt

#'/usr/bin/time' -o time_stats_run1.txt -a -f '%e %U %S' ./matrix_multiply_parallel 2000_2000_int_matrix.dat 2000

echo "Should be running on a 16-core host. (8 cores 16 siblings; like vmps902)"

echo "\n"
echo "Deleting previous time_stats data file!" 
rm time_stats_run1.txt

echo "Beginning Initial Run. Using 1 thread. For 2000, 4000, and 8000 matrix sizes."
./run_1.sh 1

echo "Beginning Next Run. Using 4 threads. For 2000, 4000, and 8000 matrix sizes."
./run_1.sh 4

echo "Beginning Next Run. Using 8 threads. For 2000, 4000, and 8000 matrix sizes."
./run_1.sh 8

echo "Beginning Next Run. Using 16 threads. For 2000, 4000, and 8000 matrix sizes."
./run_1.sh 16

echo "Beginning Next Run. Using 32 threads. For 2000, 4000, and 8000 matrix sizes."
./run_1.sh 32

