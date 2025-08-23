DEFAULT=talk-slides.pdf

all: slides.pdf

slides.pdf: $(DEFAULT)
	cp $(DEFAULT) slides.pdf

PUBLIC=../../website/slides/
LATEX2=lualatex-dev

%.pdf: %.tex .FORCE
	latexrun -W no-overfull --latex-cmd=$(LATEX) --latex-args=-shell-escape $<

talk-slides2.pdf: talk-slides2.tex .FORCE
	latexrun -W no-overfull --latex-cmd=$(LATEX2) --latex-args=-shell-escape talk-slides2.tex

test2.pdf: test2.tex .FORCE
	latexrun -W no-overfull --latex-cmd=$(LATEX2) --latex-args=-shell-escape talk-slides.tex

clean:
	latexrun --clean-all

.FORCE:

.PHONY: all clean .FORCE 

# vim: ft=make
