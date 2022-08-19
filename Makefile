#Makefile pa' la thesis guay que me hará MSc

TEX=$(wildcard *.tex */*.tex bibl/*.bib)
PYPLOT=$(wildcard 3/img/*py 4/plots/basis/*py 4/plots/promelf/*py 4/plots/theory_level/*py)
MAIN=tesis.tex
LATEX=pdflatex
PYTHON=python3
#SHELL=/bin/zsh

all: plots tex

plots:                            ## Build python plots
	$(PYTHON) $(PYPLOT)

tex:                              ## Build tex thesis (LaTeX)
	$(LATEX) $(MAIN)                # main run
	bibtex $(MAIN:.tex=)            # bibliography
	makeglossaries $(MAIN:.tex=)    # list of abbreviations, nomenclature
	$(LATEX) $(MAIN)
	$(LATEX) $(MAIN)

clean:
	@rm -rf */*.aux *.aux *.bbl *.blg *.glg *.glo *.gls *.ist *.log *.not *.ntt *.out *.sbl *.sym *.tld *.toc
