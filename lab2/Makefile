#comment
.PHONY: dats
dats: b1.dat b2.dat

b1.dat: texts/text1.md
    cat texts/text1.md | wc > text1.dat

b2.dat: texts/text2.md
    cat texts/text2.md | wc > text2.dat

dd: $(wildcard texts/*.md)
    touch dd

.PHONY: clean
clean:
    rm -f *.dat

