# Sorting Script for Class Materials 

[![LICENSE](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/dennisfarmer/scripts/master/LICENSE)

If you are a student who likes to keep their school files organized in folders sorted by chapter name, then this script is for you! With a little regular expression knowledge and a .txt file of chapter numbers and names, `sort_course_files.sh` is able to create directories and sort files into them based on extracted chapter numbers.

### Installation:
```zsh
wget https://raw.githubusercontent.com/dennisfarmer/scripts/master/sort_course_files/sort_course_files.sh ~/bin/sort_course_files && chmod u+x ~/bin/sort_course_files
```

### Usage:
```zsh
sort_course_files ./chapter_names.txt
```

![](preview.gif)
