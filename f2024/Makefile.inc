all: talk-slides.pdf

PUBLIC=../../../cs4457-website/slides

%.pdf: %.tex .FORCE
	latexrun -W no-overfull --latex-cmd=$(LATEX) --latex-args=-shell-escape $<

clean:
	latexrun --clean-all

copy-public: talk-slides.pdf
	cp talk-slides.pdf $(PUBLIC)/$(BASENAME).pdf

copy-public-heldback: talk-slides-heldback.pdf
	cp talk-slides-heldback.pdf $(PUBLIC)/$(BASENAME).pdf

.FORCE:

.PHONY: all clean .FORCE 

# vim: ft=make
