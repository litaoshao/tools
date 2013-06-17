#! /bin/sh

for((i=1; i<10; i=$i+1))
do
    datestr=`date -d "-$i days" +%Y%m%d`
    echo $datestr
done
