SOURCE   = Name-YEAR
MDFILE   = $(SOURCE).md
BIBFILE  = bibliography.bib
TEXFILE  = $(SOURCE).tex
PDFFILE  = $(SOURCE).pdf
TEMPLATE = rescience-template.tex

%.tex: $(MDFILE)
        # @echo "Processing $<"
	@pandoc --standalone                          \
                --filter ~/.cabal/bin/pandoc-crossref \
                --template=$(TEMPLATE)                \
                --latex-engine=xelatex                \
                --biblatex                            \
                --bibliography=$(BIBFILE)             \
                -M "crossrefYaml=crossref.yaml"       \
                --output $(TEXFILE) $(MDFILE)

%.pdf: $(TEXFILE) $(BIBFILE) $(TEMPLATE)
	@echo " [1/4] Processing $(TEXFILE) (pass 1)"
	@xelatex $(TEXFILE) > make.log

	@echo " [2/4] Processing $(BIBFILE)"
	@biber $(SOURCE) >> make.log

	@echo " [3/4] Processing $(TEXFILE) (pass 2)"
	@xelatex $(TEXFILE) >> make.log

	@echo " [4/4] Processing $(TEXFILE) (pass 3)"
	@xelatex $(TEXFILE) >> make.log

        # Remove the intermediate tex file because you're
        # not supposed to edit it.
	@rm $(TEXFILE)


all: $(PDFFILE)


# This prevents make to remove intermediate object files
# (we'll take care of it ourselves)
.PRECIOUS: %.tex

clean:
	@rm -f make.log
	@rm -f $(SOURCE).aux
	@rm -f $(SOURCE).log
	@rm -f $(SOURCE).bbl
	@rm -f $(SOURCE).bcf
	@rm -f $(SOURCE).blg
	@rm -f $(SOURCE).log
	@rm -f $(SOURCE).out
        # @rm -f $(SOURCE).pdf
	@rm -f $(SOURCE).tex
	@rm -f $(SOURCE).run.xml
