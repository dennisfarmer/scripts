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
cp copyconfig/copyconfig.sh $HOME/bin/copyconfig
chmod u+x $HOME/bin/copyconfig
```

### Example Usage:

```zsh
>> copyconfig -c ~/dotfiles/conf.json -d ~/dotfiles
 
Backed up: /home/user/.condarc
       to: /home/user/dotfiles/condarc
Backed up: /home/user/.config/zsh/.zshrc
       to: /home/user/dotfiles/zshrc
       ...
       ...
```

### Manual Guide:

<hr>

```
Usage:
  copyconfig [-c FILE] [-d DIRECTORY] [-r -i]

Backs up Unix configuration files as specified by copyconfig.json

ARGUMENTS-----------------------------------------------
  -h, --help               Display this message

  -c, --config <file>      Change path to config file
                           (default='./copyconfig.json')

  -d, --dotfile <folder>   Specify directory that dotfiles
                           are contained in (default='.')

  -r, --remove             Optional flag that removes
                           previously copied dotfiles

  -i, --install            Instead of copying from the
                           system to dotfile directory,
                           copy contents of dotfile directory
                           to respective system folders     

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
