find solutions -maxdepth 1 -mindepth 1 | sort -V | while read file ; do jq --arg f $file '"\($f),\(.solution),\(.time)"' $file | tr -d '"' >> solutions.csv ; done
