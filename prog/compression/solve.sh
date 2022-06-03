#!/bin/bash

# we leverage 7z's capability to extract anything
# it creates some junk @paxheader files but we don't care

e=1
arr=("gz" "xz" "zip" "bz2" "tar")

cd ./src

while [ $e -ne 0 ]
do
    f=`ls ./flag*`
    ext=${f##*\.}
    echo $ext
    if [[ " ${arr[*]} " =~ " ${ext} " ]] ; then
	7z x -y $f &> /dev/null 
	rm $f
    else
	e=0
    fi
done
