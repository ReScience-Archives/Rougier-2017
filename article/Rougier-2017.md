---
Title: "Weighted Voronoi Stippling"
Author:
  - name: Nicolas P. Rougier
    affiliation: 1,2,3
    ORCID: 0000-0003-0330-9428
Address:
  - code:    1
    address: INRIA Bordeaux Sud-Ouest, Bordeaux, France.
  - code:    2
    address: LaBRI, Université de Bordeaux, Institut Polytechnique de Bordeaux,
             Centre National de la Recherche Scientifique, UMR 5800, Talence, France.
  - code:    3
    address: Institut des Maladies Neurodégénératives, Université  de Bordeaux,
             Centre National de la Recherche Scientifique, UMR 5293, Bordeaux, France.
    
Contact:
  - Nicolas.Rougier@inria.fr
Editor:
  - Name Surname
Reviewer:
  - Name Surname
  - Name Surname
Publication:
  received:  Feb, 1, 2017
  accepted:  Feb, 1, 2017
  published: Feb, 1, 2017
  volume:    "**3**"
  issue:     "**1**"
  date:      Feb 2017
Repository:
  article:   "http://github.com/rescience/rescience-submission/article"
  code:      "http://github.com/rescience/rescience-submission/code"
  data:      "http://github.com/rescience/rescience-submission/data"
  notebook:  
Reproduction:
  - "Weighted Voronoi Stippling, Adrian Secord. In: Proceedings of the 2Nd
     International Symposium on Non-photorealistic Animation and
     Rendering. NPAR ’02. ACM, 2002, pp. 37– 43."
Bibliography:
  Rougier-2017.bib
---

# Introduction

Adrian Secord introduces in [@Secord:2002] a *techniques for generating stipple
drawings from grayscale images using weighted centroidal Voronoi diagrams* as
in *the traditional artistic technique of stippling that places small dots of
ink onto paper such that their density give the impression of tone*. The paper
is not accompanied by any code and, even though
the [webpage](http://www.mrl.nyu.edu/~ajsecord/stipples.html) of the author
points to a code archive, this one is actually nowhere to be found. We decided
to replicate the method because it can be used for different purpose, especially
in computational biology or neuroscience where the distribution of a cell
population can be conveniently described by shades of grey. It is to be noted
that since the publication of this paper, a number of related techniques have
been
proposed [@AscencioLopez:2010][@Balzer:2009a][@Balzer:2009b][@Bridson:2007]
that may be more efficient but with lower quality. We thus privileged this
implementation that is simple and provides high stippling quality.

# Methods

We applied the method proposed in the original paper with some variations due
to the non-use of the GPU for computing the Voronoi diagram. In the original
article, author computes the Voronoi diagram by taking advantage of the graphic
card (GPU) and the fact that a set of cones seen from above actually represents
a Voronoi diagram (see [@Hoff:1999]). We use instead
the [QHull](http://www.qhull.org) library (through
the [Scipy](https://scipy.github.io) Python package) for computing the Voronoi
diagram together with the Voronoi regions (as a list of segments). We also took
care of adding extra points such that each cell is contained within a
user-defined bounding box that will be set to the dimension of the density
image. For computing the weighted centroid, we applied the definition proposed
in the original paper over the discrete representation of the domain:

$${\bf C}_i = \frac{\int_A {\bf x}\rho({\bf x})dA}{\int_A \rho({\bf x})}$$

However, we did not use the proposed optimization. Instead, each cell is
rasterized (as a set of pixels) and the centroid is computed using the
integrals over the whole set of pixels composing the Voronoi cell. As noted by
the author, the precision of the method is directly related to the size of the
Voronoi cell. Consequently, if the original density image is too small
relatively to the number of stipples, there might be quality issues. Finally,
we used a fixed number of iteration ($n=50$) instead of using the difference in
the standard deviation of the area of the Voronoi regions as in the original
paper since the definition of the rejection criterion was not clear in the
original article and quite arbitrary.

# Results

We contacted the original author asking for permission to re-use
the
[original images](http://cs.nyu.edu/~ajsecord/npar2002/StipplingOriginals.zip)
but did not obtain any response. We thus display here only the output of our
replication to be compared with the original ones. The climbing shoe (figure
@fig:shoe) and the corn plant (figure @fig:corn) are very similar to the images
displayed in the original article. However, for the large and small Peperomia
plants (figure @fig:large-plant & @fig:small-plant), the output of our
replication is clearly at a lower quality without having identified the
cause. Most probably, the limited resolution of the input image may be a
critical factor and it is not clear if the author used these small resolution
versions or if he used higher resolutions.

![Climbing shoe (1300x1300), 5 000 dots, 50 iterations, point size 3](./shoe_1300x1300_org-stipple.pdf){#fig:shoe}

![Corn plant (991x934), 20 000 dots, 50 iterations, point size 1.5](./plant4h-stipple.pdf){#fig:corn}

![Large Peperomia plant (700x700), 20 000 dots, 50 iterations, point size 2.0](./plant5_700x700-stipple.pdf){#fig:large-plant}

![Small Peperomia plant (400x400), 20 000 dots, 50 iterations, point size 1.0](./plant2_400x400-stipple.pdf){#fig:small-plant}


We also provide a new set of data that is freely usable for future comparison
(CC0 licence).

![Boots (1280x853), 20 000 dots, 50 iterations, variable point size \[0.5,2.5\]](./boots-montage.png){#fig:boots}

![Pot plant (1195x1024), 20 000 dots, 50 iterations, variable point size \[0.5,2.0\]](./pot-plant-montage.png){#fig:pot-plant}

![Leafs (1195x1024), 20 000 dots, 50 iterations, variable point size \[0.5,2.0\]](./leafs-montage.png){#fig:leafs}


# Conclusion

Most of the results have been replicated even though some discrepancies remain
in the final output. Without further contact with the original author, it is
difficult to identify the precise cause but most likely, the problem occurs
because of the very limited resolution of the input picture.


# References
