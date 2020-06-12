#!/usr/bin/env bash

config_dir="."
remove=""
dotfile_dir="."

while test $# -gt 0; do
           case "$1" in
                -h|--help)
                     cat "./readme.md" 2>/dev/null | tail -n36 | head -n35 || {
                     echo "Usage:"
                     echo "  copyconfig [-c FILE] [-d DIRECTORY] [-r]"
                     echo ""
                     echo "Copies Unix configuration files as specified by copyconfig.json"
                     echo ""
                     echo "ARGUMENTS-----------------------------------------------"
                     echo "  -h, --help               Display this message"
                     echo "                          "
                     echo "  -c, --config <file>      Change path to copyconfigrc"
                     echo "                           (default='./copyconfig.json')"
                     echo ""
                     echo "  -d, --dotfile <folder>   Specify directory that dotfiles"
                     echo "                           are contained in (default='.')"
                     echo ""
                     echo "  -r, --remove             Optional flag that removes"
                     echo "                           previously copied dotfiles"
                     echo ""
                     echo "COPYCONFIG.JSON-FORMAT----------------------------------"
                     echo "_____________________________________"
                     echo '"FileName" : "Directory/FileName"'
                     echo ""
                     echo "{"
                     echo '"zshrc" : "\$HOME/.config/zsh/.zshrc",'
                     echo " ...          ..."
                     echo "}"
                     echo "_____________________________________"
                     echo ""
                     echo "Be sure to specify enviromental variables (\$ZDOTDIR, for"
                     echo "example) in ~/.bashrc or with any other similar method:"
                     echo ""
                     echo ">> vim ~/env"
                     echo '   export ZDOTDIR="\$HOME/.config/zsh"'
                     echo ""
                     echo ">> source ~/env"
                     echo ""
                     }
                     exit 0
                     ;;
                 -c|--config)
                     shift
                     config_dir=$1
                     shift
                     ;;
                 -d|--dotfile|--dotfiles)
                     shift
                     dotfile_dir=$1
                     shift
                     ;;
                 -r|--remove)
                     shift
                     remove="TRUE"
                     ;;
                 *)
                    echo "copyconfig: invalid option -- '$1'"
                    echo "Try 'copyconfig --help' for more information"
                    exit 1;
                    ;;
           esac
   done  
		      
for key in $(jq 'keys | .[]' copyconfig.json); do
    filepath=$(eval "echo $(jq .$key copyconfig.json)") 
    
    if [ $remove ]
    then
	#rm -f "$filepath"
	echo "REMOVE --> $filepath"
    else
	#[[ ! -d $key ]] $$ mkdir -p $key
	#cp -l "$dotfile_dir/$key" "$filepath"
	echo "$key --> $filepath"
    fi
done
