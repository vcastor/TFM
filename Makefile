#Makefile pa' la thesis guay que me hará MSc

TEX=$(wildcard *.tex */*.tex bibl/*.bib)
PYPLOT=$(3/img/*py 4/plots/basis/*py 4/plots/promelf/*py 4/plots/theory_level/*py)
MAIN=tesis.tex
LATEX=pdflatex
PYTHON=python3
SHELL=/bin/zsh

ALL=$(TEX) $(PYPLOT)

plots:                            ## Build python plots
	$(PYTHON) $(PYPLOT)

tex:                              ## Build tex thesis (LaTeX)
	$(LATEX) $(MAIN)                # main run
	bibtex $(MAIN:.tex=)            # bibliography
	makeglossaries $(MAIN:.tex=)    # list of abbreviations, nomenclature
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)

all:                              ## Build full thesis (LaTeX + figures)
	$(PYTHON) $(PYPLOT)
	$(LATEX) $(MAIN)                # main run
	bibtex $(MAIN:.tex=)            # bibliography
	makeglossaries $(MAIN:.tex=)    # list of abbreviations, nomenclature
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)
