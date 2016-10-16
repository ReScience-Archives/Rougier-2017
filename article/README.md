### Important

Don't forget to change the name of the Name-YEAR file to reflect all the
authors name and the current year.

### Required tools for producing the pdf

You'll need [pandoc](http://pandoc.org) (a universal document converter) and a
full [TeX distribution](https://www.tug.org/texlive/).

For pandoc, you'll also need the
[pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) filter that you can
easily install with:

```
$ cabal update
$ cabal install pandoc-crossref
```

### How to build the PDF ?

In a console, type:

```
pandoc --standalone --filter ~/.cabal/bin/pandoc-crossref --template=rescience-template.tex --latex-engine=xelatex --biblatex --bibliography=bibliography.bib -M "crossrefYaml=crossref.yaml" --output Name-YEAR.tex Name-YEAR.md
xelatex Name-YEAR
biber Name-YEAR
xelatex Name-YEAR
xelatex Name-YEAR
```

Alternativaley, you can also type `make` after having edited the Makefile.
