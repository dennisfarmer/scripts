#!/usr/bin/env bash

powerpoint_regex="LarCalcETF7e_\([0-9]\{2\}\)_[0-9]\{2\}\.pptx"
mp4_regex="\([0-9]\{1,2\}\)_[0-9]\{1,2\}.*\.mp4"

function find_dir () {
	for directory in ./*/; do
		if [[ ${directory#./} =~ $1 ]]; then
			echo $directory | rev | cut -f2- -d/ | rev
			break
		fi
	done	
}

while read p; do
	line_number=$(printf "%02d" $(echo $p | sed "s/[^[0-9]]*//g"))
	p=$(echo $p | sed "s/[0-9]*/$line_number/; s/\://g; s/\s/_/g; s/\,//g" | tr [:upper:] [:lower:]) 
	mkdir $p 2>/dev/null && echo "Creating: \"$p\"..."
done <$1

for powerpoint in ./*.pptx; do
	unit_number=$(echo  ${powerpoint#./} | sed "s/$powerpoint_regex/\1/")
	mv $powerpoint $(find_dir $unit_number)*
done

for mp4file in ./*.mp4; do
	unit_number=$(printf "%02d" $(echo ${mp4file#./} | sed "s/$mp4_regex/\1/"))
	mv $mp4file $(find_dir $unit_number)*

done
