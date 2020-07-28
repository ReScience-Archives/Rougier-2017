#! /usr/bin/env python3
# -----------------------------------------------------------------------------
# Traveling Salesperson Solver
# Tumas Rackaitis, 2020
#
# Application of:
#   Concorde TSP solver (by William Cook, 2002) and Weighted Vornoi Stippling, by
#    Nicolas P. Rougier(2017),
# -----------------------------------------------------------------------------
import numpy as np
import pandas as pd
from matplotlib import collections as mc
from concorde.tsp import TSPSolver
import matplotlib.pyplot as plt
import time
import pylab as pl
import argparse

# Arguments: dat_file String, ending in .npy. Output of stipple.py
# Returns: A tuple containing pandas DF of cities and numpy array of tour_data.
# Solves TSP instance in .dat file


def solve_tsp(dat_file, time_bound=60, verbose=True, norm="EUC_2D", seed=42):
    image_np = np.load(dat_file)
    cities = pd.DataFrame(image_np, columns=["X", "Y"])
    # solve the TSP.
    solver = TSPSolver.from_data(cities.X, cities.Y, norm="EUC_2D")
    t = time.time()
    tour_data = solver.solve(time_bound=60, verbose=True, random_seed=42)
    print(f"Finding solution took: {time.time()-t}")
    print(f"Found Tour: {tour_data.found_tour}")
    return cities, tour_data
# Plots TSP instance. Returns null.


def plot_tsp(tour_data, cities, filename="", output_prefix='output_', display=True, save=True):
    lines = [[(cities.X[tour_data.tour[i]], cities.Y[tour_data.tour[i]]),
              (cities.X[tour_data.tour[i+1]], cities.Y[tour_data.tour[i+1]])]
             for i in range(0, len(cities)-1)]
    lc = mc.LineCollection(lines, linewidths=1, colors=(0, 0, 0))
    fig, ax = pl.subplots(figsize=(20, 20))
    ax.set_aspect('equal')
    ax.add_collection(lc)
    ax.autoscale()
    if save:
        plt.savefig(output_prefix+filename+".png")
    if display:
        plt.show()


if __name__ == "__main__":
    description = "TSP art from stippled image generator"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("filename", metavar=".dat/.npy filename",
                        type=str, help='location of .dat/.npy filename, output of stipple.py')
    parser.add_argument('--time_bound', metavar='n', type=int,
                        default=60, help='Upperbound for TSP solver to find solution.')
    parser.add_argument("--verbosity", metavar="bool", type=bool,
                        default=True, help="Verbosity of TSP solver.")
    parser.add_argument("--norm", metavar="str", type=str,
                        default="EUC_2D", help="edge weight for TSP solver")
    parser.add_argument('--save', action='store_true',
                        default=True,
                        help='Save computed points')
    parser.add_argument('--display', action='store_true',
                        default=True,
                        help='Display final result')
    parser.add_argument('--output_filename',
                        type=str,
                        default="TSP",
                        help='Solved filename')             
    args = parser.parse_args()
    dat_file = args.filename
    cities, tour_data = solve_tsp(
        dat_file, time_bound=args.time_bound, verbose=args.verbosity)
    plot_tsp(tour_data, cities, filename=args.output_filename,
             display=args.display, save=args.save)
