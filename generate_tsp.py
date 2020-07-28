#! /usr/bin/env python3

import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", metavar="filepath",
                        type=str, help='location of source image')
    args = parser.parse_args()
    filepath = args.filepath
    os.system(f"python3 code/stippler.py {filepath} --save --force --n_point 20000 --n_iter 50")
    os.system(f"python3 code/tsp.py {filepath[:-4]}_stipple.npy")