#!/bin/bash
for i in {1..25}
do
    mkdir "${i}"
    cd "$i"
    LINE1="file1 = open('${i}.txt', 'r')"
    LINE2="input = file1.read().splitlines()"
    printf '%s\n' "$LINE1" "$LINE2" > "${i}.py"
    touch "${i}.txt"
    touch "${i}d.txt"
    cd ..
done