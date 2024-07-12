SLIDEDECKS = \

all: $(patsubst %,_dist/%.pdf,$(SLIDEDECKS))

clean:
	rm -r _dist

_dist:
	mkdir _dist

_dist/%.pdf: % _dist
	cd $< && make && cp talk-slides.pdf ../dist/$<.pdf

.PHONY: all
