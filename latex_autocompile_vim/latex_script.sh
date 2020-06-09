#!/usr/bin/env bash

# Allows editing of files not in current directory
current_directory=$(pwd)
file_directory=$(echo $1 | rev | cut -d/ -f2- | rev)

file=$(echo $1 | rev | cut -f2- -d. | rev) #Filename without any extention 

file_isopen=`ps -fe | grep "$PDFVIEWER $(echo $file).pdf" | grep -vc grep` #=0 if instance not found in ps

cd $file_directory

pdflatex $1 >/dev/null 2>&1 &

if [ $file_isopen -eq 0 ]; then
	$PDFVIEWER $file".pdf" 
fi

sleep 2; rm $file".aux" $file".log" 2>/dev/null

cd $current_directory
