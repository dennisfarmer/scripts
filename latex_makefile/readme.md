# LaTeX Makefile

[![LICENSE](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/dennisfarmer/scripts/master/LICENSE)

This makefile allows for intuitive autocompiling and viewing of your LaTeX files while you are editing them.

### Requirements:
`make, inotify-tools, texlive`

_Additional:_

* `vim` [or some other terminal text editor that will totally impress the coffee store barista]
* `okular` [or equivalent pdf reader with update-on-save capabilities]
* Using `tmux` is highly recommended (for convenience) but not required

### Usage:

* Move `Makefile` to your LaTeX project directory
* Change the `$TEX` variable in `Makefile` to the name of your main document (ending in `.tex`, `.xtx`, etc.)
* Open your main document in Vim (or something else, I guess...) and run `make watch` in a seperate terminal window or new tmux window
* Whenever you save your document, it will automatically be compiled into a viewable `.pdf`
* Optional: run `make clean` when done editing to remove extra files

_Note:_ If you are using `bash` instead of `zsh` as your shell, be sure to change the `$SHELL` variable in the makefile as well as comment out the ZSH line and uncomment the BASH line under the `watch` command. For other shells, just find the respective syntax for an infinite while loop and stick it at the beginning of the line, as the loop syntax is likely the only part that will change between shells.

_If you're feeling even lazier than I am, feel free to adapt my old hacky script into this makefile to make your pdf reader auto-open upon running_ `make watch` _._


