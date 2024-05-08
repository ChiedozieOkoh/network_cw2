#!/bin/bash
echo "===start==="
stamp="timestamp=$(date +%s)"
echo $stamp
cat $1 | while read -r line ; do
   echo " "
   traceroute $line
done

echo "===end==="
