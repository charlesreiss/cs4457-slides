SLIDEDECKS = \
    intro \
    framing \
    physical \
    reliable


all: $(patsubst %,_dist/%.pdf,$(SLIDEDECKS))

clean:
	rm -r _dist

_dist:
	mkdir _dist

_dist/%.pdf: % _dist
	cd $< && make && cp talk-slides.pdf ../_dist/$<.pdf

.PHONY: all
