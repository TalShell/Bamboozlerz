#! /usr/bin/env python3

from library import Library
from book import Book
from multiprocessing import Pool
import random,math

def checklib(l,explored_libs,d,allBooks,explored_book):
    if l.sinupDate >=d:
        ship=0
        for bk in l.unique_books:
            if ship >= l.ship:
                break
            if not bk.id in allBooks:
                l.score -=bk.score
                bk.is_scanned=True
                l.score -=bk.score
                allBooks.add(bk.id)
                l.scanned_book +=1
                l.booktokeep.append(bk.id)
                explored_libs.add(l)
                explored_book.add(bk.id)
                ship+=1

                
def process(books, libs, days,explored_libs,explored_book):
    startDate=0;
    print(days)
    allBooks = set()
    mainBooks = set()
    
    #Assign to each library a score 
    for l in libs:
        for bk in l.unique_books:
            if bk.id not in mainBooks:
                mainBooks.add(bk.id)
                l.score = l.score + bk.score
        l.unique_books.sort(key=lambda x: x.score, reverse=True)
        l.max_score=l.unique_books[0].score
        #print(l.max_score)
            
    #libs.sort(key=lambda x: math.sqrt(x.score), reverse=False)
    random.shuffle(libs)
    
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
    print('MaxDay:',days)

    for d in range(days):
        #print('Day:',d)
        for l in libs:
            checklib(l,explored_libs,d,allBooks,explored_book)
        if len(mainBooks) == len(allBooks):
            print('Stop as all books were scanned')
            break
        #libs.sort(key=lambda x: (x.score)/(len(x.booktokeep)+1), reverse=True)
        libs.sort(key=lambda x: len(x.booktokeep)-len(x.unique_books), reverse=False)

