# LaTeX Makefile
# Dependencies: inotify-tools texlive

TEX=dennis_farmer_resume_2020.tex # document.xtx
SHELL=/bin/zsh

compile:
	xelatex $(TEX)

clean:
	rm $(TEX).aux $(TEX).log $(TEX).out

watch:
	# ZSH:
	@while [ 1 ]; do; inotifywait $(TEX); sleep 0.01; make compile; done
	# BASH:
	# @while true; do; inotifywait $(TEX); sleep 0.01; make compile; done

