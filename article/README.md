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
pandoc --standalone --filter ~/.cabal/bin/pandoc-crossref --template=rescience-template.tex --latex-engine=xelatex --biblatex --bibliography=Rougier-2017.bib -M "crossrefYaml=crossref.yaml" --output Rougier-2017.tex Rougier-2017.md
xelatex Rougier-2017
biber Rougier-2017
xelatex Rougier-2017
xelatex Rougier-2017
```

Alternativaley, you can also type `make` after having edited the Makefile.
