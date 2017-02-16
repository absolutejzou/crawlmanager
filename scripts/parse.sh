#!/bin/sh
# 用来解析配置文件,并将其配置到环境变量中

if [ $# != 1 ];then
    echo "USAGE: $0 config_file"
    exit 1
fi

file=$1
if [ ! -f "$file" ];then
    echo "no such file: $file"
    exit 1;
fi

areas=`sed -n '/^\[/=' $file`

nums=$( echo $areas |tr " " "\n")
i=0
for num in $nums
do
    area_num_array[$i]=$num
    ((i=i+1))
done

length=${#area_num_array[@]}


j=0
while [ $j -lt $length ]
do
    num=${area_num_array[j]}
    area_name=`sed -n "$num,$num p" $file | sed 's/\[//g' | sed 's/\]//g'`
    ((next=j+1))
    ((start=num+1))

    if [ $next != $length ];then
        next_num=${area_num_array[$next]}
        ((end=next_num-1))
        area=`sed -n "$start,$end p" $file | sed  '/^$/d' | sed '/^\#/d' | sed 's/ //g'`
    else
        area=`sed -n "$start,$ p" $file | sed  '/^$/d' | sed '/^\#/d' | sed 's/ //g'`
    fi

    params=$(echo $area | tr " " "\n")

    for param in $params
    do
        key=`echo $param | awk -F '=' '{print $1}'`
        value=`echo $param | awk -F '=' '{print $2}'`
        v_name=$area_name'_'$key
        eval export $v_name=$value
    done
    ((j=j+1))
done

