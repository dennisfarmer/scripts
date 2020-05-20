#!/usr/bin/env bash

config_dir="./copyconfigrc"
remove=""
dotfile_dir="."

files=()
dirs=()

while test $# -gt 0; do
           case "$1" in
                -h|--help)
                    cat "./readme.md" 2>/dev/null | sed -ne " /\`\`\`/,$ p" | sed " /\`\`\`/ d" || {
                    echo "Usage:"
                    echo "  copyconfig [-c FILE] [-d DIRECTORY] [-r]"
                    echo ""
                    echo "Copies Unix configuration files as specified by copyconfigrc"
                    echo ""
                    echo "ARGUMENTS-----------------------------------------------"
                    echo "  -h, --help               Display this message"
                    echo ""                          
                    echo "  -c, --config <file>      Change path to copyconfigrc "
                    echo "                           (default='./copyconfigrc')"
                    echo ""                          
                    echo "  -d, --dotfile <folder>   Specify directory that dotfiles"
                    echo "                           are contained in (default='.')"
                    echo ""                          
                    echo "  -r, --remove             Optional flag that removes"
                    echo "                           previously copied dotfiles"
                    echo ""
                    echo "COPYCONFIGRC-FORMAT-------------------------------------"
                    echo "___________________________________"
                    echo "File Name   Configuration Directory"
                    echo ""
                    echo ".zshrc      \$HOME/.config/zsh"
                    echo " ...          ..."
                    echo "___________________________________"
                    echo ""
                    echo "Be sure to specify enviromental variables (\$ZDOTDIR, for"
                    echo "example) in ~/.bashrc or with any other similar method:"
                    echo ""
                    echo ">> vim ~/env"
                    echo '   export ZDOTDIR="$HOME/.config/zsh"'
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

# parse copyconfigrc for filename and configuration directory
while read line; do
#   remove comments
    line=$(echo "$line" | sed "s/#.*//g; /^$/ d" )

    files+=( $(echo "$line" | awk '{print $1}') )
    
#   convert $HOME to /home/user, etc...
    dir_text=$(echo "$line" | awk '{print $2}') 
    global_var=$(echo $dir_text | sed "s|^\(\$[^\/]*\).*$|\1|")
    converted_var=$(eval "echo $global_var")
    dirs+=( $(echo $dir_text | sed "s|\(\$[^\/]*\)|$converted_var|") )
done < "$config_dir"

# remove or copy dotfiles to specified directory
for i in ${!dirs[@]}; do
    f=${files[$i]}; d=${dirs[$i]}
    
    if [ $remove ]
    then
        rm -f "$d/$f"
        echo "REMOVE --> $d/$f"
    else
        [[ ! -d $d ]] && mkdir -p $d
        cp -l "$dotfile_dir/$f" "$d/$f"
        echo "$f --> $d/$f"
    fi
done
