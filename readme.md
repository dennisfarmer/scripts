# CopyConfig
This shell script is a sorta hacky way to automatically update system configuration files from a central folder without having to keep track of where they are all located on your system. 

Using a file called `copyconfigrc`, you can specify each of your files along with the directory you want them to be placed in.

Github integration will be added later to allow you to automatically pull dotfiles from a repository.

## Installation and Setup:

`git clone https://github.com/dennisfarmer/copyconfig.git`

`cd copyconfig`

`chmod u+x copyconfig.sh` 

## Example Useage:

        >> sh copyconfig.sh -d ~/Dotfiles
        
        bash_aliases --> /home/dennisfarmer/bash_aliases
        .zshrc --> /home/dennisfarmer/.config/zsh/.zshrc
        vimrc --> /home/dennisfarmer/.vim/vimrc

## Manual Guide:

<hr>

```
Usage:
  copyconfig [-c FILE] [-d DIRECTORY] [-r]

Copies Unix configuration files as specified by copyconfigrc

ARGUMENTS-----------------------------------------------
  -h, --help               Display this message
                          
  -c, --config <file>      Change path to copyconfigrc
                           (default='./copyconfigrc')

  -d, --dotfile <folder>   Specify directory that dotfiles
                           are contained in (default='.')

  -r, --remove             Optional flag that removes
                           previously copied dotfiles

COPYCONFIGRC-FORMAT-------------------------------------
___________________________________
File Name   Configuration Directory

.zshrc      $HOME/.config/zsh
 ...          ...
___________________________________

Be sure to specify enviromental variables ($ZDOTDIR, for
example) in ~/.bashrc or with any other similar method:

>> vim ~/env
   export ZDOTDIR="$HOME/.config/zsh"

>> source ~/env
 
```
