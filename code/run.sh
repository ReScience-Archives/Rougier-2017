#!/bin/sh

# ---------------------------------------------------------------------------
# In order to run the following examples, you will need original images from
# http://cs.nyu.edu/~ajsecord/npar2002/StipplingOriginals.zip
# ---------------------------------------------------------------------------

./stippler.py ../data/original/plant2_400x400.png --force --save \
              --n_point 20000 --n_iter 50 --pointsize 1.0 1.0 --figsize 6

./stippler.py ../data/original/plant5_700x700.png --force --save \
              --n_point 20000 --n_iter 50 --pointsize 1.5 1.5 --figsize 8

./stippler.py ../data/original/plant4h.png --force --save \
              --n_point 20000 --n_iter 50 --pointsize 1.5 1.5 --figsize 8

./stippler.py ../data/original/shoe_1300x1300_org.png --force --save \
              --n_point 5000 --n_iter 50 --pointsize 3. 3. --figsize 6


# ---------------------------------------------------------------------------
# These example use CC0 images
# ---------------------------------------------------------------------------
./stippler.py ../data/boots.jpg --save --force \
              --n_point 20000 --n_iter 50 --pointsize 0.5 2.5 --figsize 8

montage -geometry 1500 -tile 1x2 -mode concatenate \
        boots.jpg boots-stipple.png boots-montage.png

./stippler.py ../data/pot-plant.jpg --save --force \
              --n_point 20000 --n_iter 50 --pointsize 0.5 2.0 --figsize 8

./stippler.py ../data/plant.jpg --save --force \
              --n_point 20000 --n_iter 50 --pointsize 0.5 2.0 --figsize 8

./stippler.py ../data/gradient.png --save --force \
              --n_point 5000 --n_iter 50 --pointsize 1.0 1.0 --figsize 8
