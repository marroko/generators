#!/bin/bash

DIR=$1
MEASUREMENTS=$2

if [ "$#" -ne 2 ]; then
    echo "Usage: ./time_cat.sh directory measurements_count"
    exit
fi

FILE_BEFORE=${DIR}/${DIR}_time_cat_before.txt
FILE_AFTER=${DIR}/${DIR}_time_cat_after.txt

for ((i = 0; i < $MEASUREMENTS; i++)) do
    if [ $i -eq 0 ]; then
        time ( cat $DIR/*before.[ch]pp ) 2> $FILE_BEFORE
        time ( cat  $DIR/*after.[ch]pp ) 2> $FILE_AFTER 
    else
        time ( cat $DIR/*before.[ch]pp ) 2>> $FILE_BEFORE
        time ( cat $DIR/*after.[ch]pp ) 2>> $FILE_AFTER
    fi 
done

TIME_BEFORE=`grep "real" $FILE_BEFORE | cut -f 2 | tr -d 'ms' | awk '{sum+=$1}; END {printf "%.3f\n", sum}'`
TIME_AFTER=`grep "real" $FILE_AFTER | cut -f 2 | tr -d 'ms' | awk '{sum+=$1}; END {printf "%.3f\n", sum}'`

AVG_BEFORE=$(echo "scale=4; $TIME_BEFORE/$MEASUREMENTS" | bc)
AVG_AFTER=$(echo "scale=4; $TIME_AFTER/$MEASUREMENTS" | bc)

echo "AVG_BEFORE: $AVG_BEFORE" | tee -a $FILE_BEFORE
echo "AVG_AFTER: $AVG_AFTER" | tee -a $FILE_AFTER
