#!/usr/bin/env bash
log_file="script_output.log"
> "$log_file"
script_content='
n=$(( RANDOM % 100 ))
if [[ n -eq 42 ]]; then
   echo "Something went wrong"
   >&2 echo "The error was using magic numbers"
   exit 1
fi
echo "Everything went according to plan"
'
count=0
while true; do
    bash -c "$script_content" >> "$log_file" 2>&1
    if [[ $? -ne 0 ]]; then
        break
    fi
    count=$((count + 1))
done
echo "count: $count"
cat "$log_file"
