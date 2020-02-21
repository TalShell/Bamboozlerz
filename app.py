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
        libs.append(Library(lib_id,signup, ship, libbooks))
        lib_id = lib_id + 1

    score = 0
    explored_libs=set()
    explored_book =set()
    print('len(explored_libs) :', len(explored_libs))
    while(score < 4) :
        explored_books=0
        score =0
        explored_libs.clear()
        explored_book.clear()
        print('Starting NbrLib Expl',len(explored_libs))
        print('Starting score :', score)
        print('Starting Explored ',explored_books)
        for l in libs:
                l.score = 0
                l.scanned_book=0
                l.booktokeep.clear()
                l.max_score=0
                l.sinupDate=0
                for b in l.unique_books:
                    b.is_scanned=False
        
        process(books, libs, days,explored_libs,explored_book)
    
        print('NbrLib ',len(libs))
        print('NbrBook ',len(books))

        for b in explored_book :
            score += books[b].score
            explored_books +=1
    
        print('Explored ',explored_books)
        print('NbrLib Expl',len(explored_libs))

        print("score: ",score)
        
    generate_output(fileout, explored_libs)

def generate_output(fileout, outlibs):
    fileout.write(str(len(outlibs)))
    fileout.write("\n")
    for lib in outlibs:
        if lib.scanned_book > 0:
            fileout.write("{} {}\n".format(lib.id, lib.scanned_book))
            #fileout.write(' '.join(map(lambda x: str(x.id) if x.is_scanned else "", lib.unique_books))+ "\n") 
            fileout.write(' '.join(map(str,  lib.booktokeep))+ "\n") 
        

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
