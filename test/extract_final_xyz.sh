#!/bin/bash
j1=$1
number_of_atoms=$(cat $j1 | grep '| Number of atoms                   :' | awk '{print $6}')
sed  -n "/Final atomic structure:/,/Performing Mulliken charge/p" $j1 >tmp
((line=number_of_atoms+2))
sed -n "3,$line"p tmp
rm tmp
