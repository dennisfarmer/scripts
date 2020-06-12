# CopyConfig

[![LICENSE](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/dennisfarmer/scripts/master/LICENSE)

This script is a sorta hacky way to automatically update system configuration files from a central folder without having to keep track of where they are all located on your system. 

Using a file called `copyconfig.json`, you can specify each of your files along with the directory you want them to be placed in.

Github integration will be added later to allow you to automatically pull dotfiles from a repository.

### Requirements:
`git, jq`

### Installation:

```zsh
git clone https://github.com/dennisfarmer/copyconfig.git

chmod u+x copyconfig/copyconfig.sh
```

### Example Usage:

```zsh
>> ./copyconfig.sh -d ~/Dotfiles
 
"tmuxrc" --> /home/dennisfarmer/.config/tmux/tmuxrc
"vimrc" --> /home/dennisfarmer/.vim/vimrc
"zshenv" --> /home/dennisfarmer/.config/zsh/.zshenv
"zshrc" --> /home/dennisfarmer/.config/zsh/.zshrc
```

### Manual Guide:

<hr>

```
Usage:
  copyconfig [-c FILE] [-d DIRECTORY] [-r]

Copies Unix configuration files as specified by copyconfig.json

ARGUMENTS-----------------------------------------------
  -h, --help               Display this message
                          
  -c, --config <file>      Change path to copyconfigrc
                           (default='./copyconfig.json')

  -d, --dotfile <folder>   Specify directory that dotfiles
                           are contained in (default='.')

  -r, --remove             Optional flag that removes
                           previously copied dotfiles

COPYCONFIG.JSON-FORMAT----------------------------------
_____________________________________
"FileName" : "Directory/FileName"

{
"zshrc" : "$HOME/.config/zsh/.zshrc",
 ...          ...
}
_____________________________________

Be sure to specify enviromental variables ($ZDOTDIR, for
example) in ~/.bashrc or with any other similar method:

>> vim ~/env
   export ZDOTDIR="$HOME/.config/zsh"

>> source ~/env
 
```
