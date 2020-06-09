# LaTeX Autocompile for Vim

This script allows you to automatically compile and preview LaTeX documents without having to leave vim. The PDF viewer used is set by the `$PDFVIEWER` global variable (A viewer with auto-update upon save, like okular, is recommended)

### Requirements:
`pdflatex, any suitable PDF viewer` 





autocmd FileType tex,latex,plaintex nnoremap <buffer> <Leader>p :w <bar> sh latex_script.sh first_document.tex ~/github/scripts/latex_autocompile_vim/latex_script.sh % & disown <CR><CR>
