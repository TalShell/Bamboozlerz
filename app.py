#! /usr/bin/env python3

def process(filein, fileout):
    pass

if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", nargs='+', type=argparse.FileType('r'))
    
    options = parser.parse_args()

    for filein in options.input:
        out = os.path.join("out", os.path.basename(filein.name))
        with open(out, "w") as fileout:
            process(filein, fileout) 