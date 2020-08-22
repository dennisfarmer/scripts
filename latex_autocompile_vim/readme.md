# LaTeX Autocompile for Vim

[![LICENSE](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/dennisfarmer/scripts/master/LICENSE)

This script allows you to automatically compile and preview LaTeX documents without leaving vim. The PDF viewer used is set by the `$PDFVIEWER` global variable (A viewer with auto-update upon save, like okular, is recommended)

### Requirements:
`svn, xelatex (or pdflatex/lualatex), okular (or equivalent)`

### Installation:
_In the following lines, replace `$SCRIPTS` with your desired scripts directory, and `$VIMRC` with the location of your vimrc._

```zsh
svn checkout https://github.com/dennisfarmer/scripts/trunk/latex_autocompile_vim $SCRIPTS

chmod u+x $SCRIPTS/latex_autocompile_vim/latex_script.sh

echo '" LaTeX Autocompile Hotkey:\nautocmd FileType tex,latex,plaintex nnoremap <buffer> <Leader>p :w <bar> sh $SCRIPTS/latex_autocompile_vim/latex_script.sh % & disown <CR><CR>' >> $VIMRC
```

### Usage:
Press `<leader> + p` from within vim to have the compiled version of the current LaTeX file open in a new window.

By default, `<leader>` is set to the `\` key, but you can change it to `Space` by placing this line in your vimrc:

```vim
let mapleader="\<Space>"
```
