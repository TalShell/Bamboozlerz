#! /usr/bin/env python3

from library import Library
from book import Book
from multiprocessing import Pool

def checklib(l,explored_libs,d,allBooks):
    if l.sinupDate >d:
        ship=0
        for bk in l.unique_books:
            if ship >= l.ship:
                break
            if not bk in allBooks :
                bk.is_scanned=True
                l.score -=bk.score
                explored_libs.add(l)
                ship+=1
                
def process(books, libs, days,explored_libs):
    startDate=0;
    print(days)
    allBooks = set()
    #Assign to each library a score 
    for l in libs:
        for bk in l.unique_books:
            l.score = l.score + bk.score
        l.unique_books.sort(key=lambda x: x.score, reverse=True)
    
    libs.sort(key=lambda x: (x.score/x.signup_days), reverse=True)
    
    fucking_days = []
    #Assign to each library a starting date
    for l in libs:
        startDate += l.signup_days
        if startDate > days:
            break
        l.sinupDate = startDate
        fucking_days.append(startDate)

    print("Sorting done")
    #Naive approach
    for d in fucking_days:
        for l in libs:
            checklib(l,explored_libs,d,allBooks)
        libs.sort(key=lambda x: (x.score/x.signup_days), reverse=True)

                    
                
