#Makefile pa' la thesis guay que me hará MSc

ALL=$(wildcard *.tex */*.tex bibl/*.bib)
MAIN=tesis.tex
LATEX=pdflatex
SHELL=/bin/zsh

all:                              ## Build full thesis (LaTeX + figures)
	$(LATEX) $(MAIN)                # main run
	bibtex $(MAIN:.tex=)            # bibliography
	makeglossaries $(MAIN:.tex=)    # list of abbreviations, nomenclature
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)
