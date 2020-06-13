#!/usr/bin/env bash

config_dir="./copyconfig.json"
remove=""
dotfile_dir="."
installing=""

while test $# -gt 0; do
           case "$1" in
                -h|--help)
                     echo "Usage:"
                     echo "  copyconfig [-c FILE] [-d DIRECTORY] [-r -i]"
                     echo ""
                     echo "Backs up Unix configuration files as specified by copyconfig.json"
                     echo ""
                     echo "ARGUMENTS-----------------------------------------------"
                     echo "  -h, --help               Display this message"
                     echo ""
                     echo "  -c, --config <file>      Change path to config file"
                     echo "                           (default='./copyconfig.json')"
                     echo ""
                     echo "  -d, --dotfile <folder>   Specify directory that dotfiles"
                     echo "                           are contained in (default='.')"
                     echo ""
                     echo "  -r, --remove             Optional flag that removes"
                     echo "                           previously copied dotfiles"
                     echo ""
                     echo "  -i, --install            Instead of copying from the"
                     echo "                           system to dotfile directory,"
                     echo "                           copy contents of dotfile directory"
                     echo "                           to respective system folders"
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
	             read -p "Are you sure you wish to REMOVE files from system directories? [y|n] " -n 1 -r
                     if [[ $REPLY =~ ^[Yy]$ ]]
	             then
	             echo "";echo ""
                     remove="TRUE"
		     fi
                     ;;
                 -i|--install)
		     shift
	             echo "Are you sure you wish to INSTALL files to system directories?"
	             read -p "This will OVERWRITE existing configuration files! [y|n] " -n 1 -r
                     if [[ $REPLY =~ ^[Yy]$ ]]
	             then
	             echo ""; echo ""
		     installing="TRUE"
		     fi
		     ;;
                 *)
                    echo "copyconfig: invalid option -- '$1'"
                    echo "Try 'copyconfig --help' for more information"
                    exit 1;
                    ;;
           esac
   done  
		      
for key in $(jq 'keys | .[]' $config_dir); do
    filepath=$(eval "echo $(jq .$key $config_dir)") 
    
    global_var=$(echo $filepath | sed "s|^\(\$[^\/]*\).*$|\1|")
    converted_var=$(eval "echo $global_var")
    filepath=$(echo $filepath | sed "s|\(\$[^\/]*\)|$converted_var|") 
    
    key=$(echo $key | sed "s/\"//g")
    
    if [ $remove ]
    then
	rm -rf "$filepath" && {
	echo "Removed: $filepath"
        }
    else
	if [ $installing ]
	then
	    file_dir=$(echo $filepath | rev | cut -d/ -f2- | rev) 
	    [[ ! -d $file_dir ]] && mkdir -p $file_dir
             
	    cp -r "$dotfile_dir/$key" $filepath && {
		    echo "Installed: $key"
		    echo "       to: $filepath"
            }
	else
	    if [ -d "$filepath" ]
	    then
		[[ ! -d "$dotfile_dir/$key" ]] && mkdir -p "$dotfile_dir/$key"
	        cp -r $filepath/* $dotfile_dir/$key && {
			echo "Backed up: $filepath"
			echo "       to: $dotfile_dir/$key"
	        }
	    else 
		cp -r "$filepath" "$dotfile_dir/$key" && {
			echo "Backed up: $filepath"
			echo "       to: $dotfile_dir/$key"
                }
	    fi

	fi
    fi
done; exit 0
