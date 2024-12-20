SLIDEDECKS = \
    logistics \
    intro \
    framing \
    physical \
    reliable \
    switches \
    arp \
    congest \
    queuing \
    routing \
    sockets \
    dns \
    http \
    multiaccess \
    fire \
    encap \
    p2p


all: $(patsubst %,_dist/%.pdf,$(SLIDEDECKS))

clean:
	rm -r _dist

_dist:
	mkdir _dist

_dist/%.pdf: % _dist .FORCE
	cd $< && make && cp talk-slides.pdf ../_dist/$<.pdf

.PHONY: all .FORCE
