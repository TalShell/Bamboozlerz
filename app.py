#! /usr/bin/env python3

from library import Library
from book import Book
from process import process

def handlein(filein, fileout):
    lines = filein.readlines()
    nb_books, nb_libs, days = map(int,lines[0].split(' '))
    books = {}
    book_scores = list(map(int,lines[1].split(' ')))
    for i in range(nb_books):
        books[i] = Book(i, book_scores[i], 0)
    libs = []
    lib_id = 0
    for i in range(2,2+2*nb_libs,2):
        capacity, signup, ship = map(int, lines[i].split(' '))
        libbooks = list(map(lambda x: books[int(x)], lines[i +1].split(' ')))
        libs.append(Library(lib_id, signup, ship, libbooks))
        lib_id = lib_id + 1
    process(books, libs)
    generate_output(fileout, libs)

def generate_output(fileout, outlibs):
    fileout.write(str(len(outlibs)))
    fileout.write("\n")
    for lib in outlibs:
        fileout.write("{} {}\n".format(lib.id, len(lib.unique_books)))
        fileout.write(' '.join(map(lambda x: str(x.id), lib.unique_books))+ "\n") 
        

if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", nargs='+', type=argparse.FileType('r'))
    
    options = parser.parse_args()

    for filein in options.input:
        out = os.path.join("out", os.path.basename(filein.name))
        with open(out, "w") as fileout:
            handlein(filein, fileout) 