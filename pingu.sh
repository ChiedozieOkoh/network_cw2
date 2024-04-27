#!/bin/bash
echo "===start==="
stamp="timestamp=$(date +%s)"
echo $stamp
cat $1 | while read -r line ; do
   echo " "
   ping $line -c 120 -W 120
   echo "<-->"
done

echo "===end==="
