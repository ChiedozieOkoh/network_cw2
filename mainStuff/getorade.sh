#!/bin/bash
echo "===start==="
stamp="timestamp=$(date +%s)"
echo $stamp
cat $1 | while read -r line ; do
   echo " "
   wget $line -O /dev/null -a $2
   echo "<-->"
done

echo "===end==="
