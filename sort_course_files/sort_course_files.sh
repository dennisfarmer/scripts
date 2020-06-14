#!/usr/bin/env bash

mp4_regex="\([0-9]\{1,2\}\)_[0-9]\{1,2\}_etf_.*\.mp4"
powerpoint_regex="LarCalcETF7e_\([0-9]\{2\}\)_[0-9]\{2\}\.ppt"

# make dirs:
while read line; do
	line_number=$(printf "%02d" $(echo $line | sed "s/[^[0-9]]*//g; s/^0*//") )
	line=$(echo $line | sed "s/[0-9]*/$line_number/; s/\://g; s/\s/_/g; s/\,//g" | tr [:upper:] [:lower:]) 
	mkdir $line 2>/dev/null && echo "Creating: \"$line\"..."
done <$1

function findDir () {
	# Find directory name that contains given string
	# $1 = pattern_to_match 

	for directory in ./*/; do
		if [[ ${directory#./} =~ $1 ]]; then
			# remove trailing "/" character
			echo $directory | rev | cut -f2- -d/ | rev
			break
		fi
	done	
}

function moveFiles () {
	# $1 = file_extention (.pptx, .mp4, ...)
	# $2 = reg_expr (to parse filename for unit number)

	for file in ./*$1; do
		unit_number=$(printf "%02d" $(echo ${file#./} | sed "s/$2/\1/; s/^0*//") )
		mv $file $(findDir $unit_number)*
	done
}
 
moveFiles ".mp4" $mp4_regex
moveFiles ".ppt" $powerpoint_regex
