all: talk-slides.pdf

PUBLIC=../../website/slides/

%.pdf: %.tex .FORCE
	latexrun -W no-overfull --latex-cmd=$(LATEX) --latex-args=-shell-escape $<

clean:
	latexrun --clean-all

.FORCE:

.PHONY: all clean .FORCE 

# vim: ft=make
