Features of This Repo:
# 1. Travelling Salesperson Art
![](article/example_tsp.png)

# 2. Weighted Voronoi Stippling

![](article/boots-montage.png)

This is a replication of the following article:

*Weighted Voronoi Stippling*, Adrian Secord. In: Proceedings of the 2nd
International Symposium on Non-photorealistic Animation and
Rendering. NPAR ’02. ACM, 2002, pp. 37– 43.

where the author introduced a *techniques for generating stipple drawings from
grayscale images using weighted centroidal Voronoi diagrams* as in *the
traditional artistic technique of stippling that places small dots of ink onto
paper such that their density give the impression of tone*.


## Setup:

This replication has been written and tested on OSX 10.12 (Sierra) using the
following packages:

 * Python 3.6.0
 * Numpy 1.12.0
 * Scipy 0.18.1
 * Matplotlib 2.0.0
 * tqdm 4.11.2
 * Pillow 4.0.0
 * Imageio 2.9.0
 ### Setup Instructions (for TSP): 
0. Make a venv for this repo (recommended). Python 3.5+ works best:
```python3 -m venv TSP  ```
1. activate the venv and use pip to install the following:
```pip3 install numpy pandas matplotlib Pillow cython ```

2. You'll need the concorde TSP solver -- one of the most powerful TSP solvers around, and to get in it python, you'll have to do the following:
  a. clone the python wrapper library 
  ```
  git clone https://github.com/jvkersch/pyconcorde
  cd pyconcorde
  ```
  b. run pip install  (dont forget the period). This may take a minute. 
  ```
  pip3 install -e .
  ```
  c. verify installation. open up the python interpreter and type:
  ```from concorde.tsp import TSPSolver ```
  And make sure it doesn't fail.
  
  
## Usage
```
usage: generate_tsp.py [-h] filepath

positional arguments:
  filepath    location of source image

optional arguments:
  -h, --help  show this help message and exit

```
```
usage: tsp.py [-h] [--time_bound n] [--verbosity bool] [--norm str] [--save]
              [--display] [--output_filename OUTPUT_FILENAME]
              .dat/.npy filename

TSP art from stippled image generator

positional arguments:
  .dat/.npy filename    location of .dat/.npy filename, output of stipple.py

optional arguments:
  -h, --help            show this help message and exit
  --time_bound n        Upperbound for TSP solver to find solution.
  --verbosity bool      Verbosity of TSP solver.
  --norm str            edge weight for TSP solver
  --save                Save computed points
  --display             Display final result
  --output_filename OUTPUT_FILENAME
                        Solved filename
```
```
 usage: stippler.py [--n_iter n] [--n_point n] [--save] [--force]
                    [--pointsize min,max] [--figsize w,h]
                    [--display] [--interactive] file

 Weighted Vororonoi Stippler

 positional arguments:
   file                  Density image filename

 optional arguments:
   -h, --help            show this help message and exit
   --n_iter n            Maximum number of iterations
   --n_point n           Number of points
   --pointsize (min,max) (min,max)
                         Point mix/max size for final display
   --figsize w,h         Figure size
   --force               Force recomputation
   --save                Save computed points
   --display             Display final result
   --interactive         Display intermediate results (slower)
```
