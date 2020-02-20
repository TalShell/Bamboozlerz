#! /usr/bin/env python3

from library import Library
from book import Book
from multiprocessing import Pool

def checklib(l,explored_libs,d,allBooks):
    if l.sinupDate >d:
        ship=0
        for bk in l.unique_books:
            if ship >= l.ship:
                print('noship')
                break
            if not bk in allBooks :
                bk.is_scanned=True
                l.score -=bk.score
                explored_libs.add(l)
                print('explored')
                ship+=1
                
def process(books, libs, days,explored_libs):
    startDate=0;
    print(days)
    allBooks = set()
    unik_books=set()

    #Assign to each library a score 
    for l in libs:

        l.nbbooks= len(l.unique_books)
        for bk in l.unique_books:
            if not bk.id in unik_books:
                l.score = l.score + bk.score
                unik_books.add(bk.id)
                print('add')
            else:
                l.nbbooks =-1
                
        l.unique_books.sort(key=lambda x: x.score, reverse=True)

    
    libs.sort(key=lambda x: x.nbbooks, reverse=False)
    
    
    
    fucking_days = []
    #Assign to each library a starting date
    for l in libs:
        if startDate +l.ship>= days:
            print('too big')
            continue
        else:
            print(startDate,l.id,l.score,l.ship)

            startDate = startDate +l.ship
            l.signup_days = startDate
            fucking_days.append(startDate)
            print(startDate,'dayz')

    print("Sorting done")
    print(len(libs),len(fucking_days))
    #Naive approach
    for d in fucking_days:
        for l in libs:
            checklib(l,explored_libs,d,allBooks)
            libs.sort(key=lambda x: (x.score/x.ship), reverse=True)

                    
                
