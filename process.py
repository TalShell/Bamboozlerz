#! /usr/bin/env python3

from library import Library
from book import Book
from multiprocessing import Pool

def checklib(l,explored_libs,d):
    if l.sinupDate <d:
        for bk in l.unique_books:
            if not bk.is_scanned:
                bk.is_scanned=True
                explored_libs.append(l)
                
def process(books, libs, days):
    explored_libs=[]
    startDate=0;
    print(days)
    
    #Assign to each library a score 
    for l in libs:
        for bk in l.unique_books:
            l.score = l.score + bk.score
        l.unique_books.sort(key=lambda x: x.score, reverse=False)
    
    libs.sort(key=lambda x: x.score, reverse=False)
    
    #Assign to each library a starting date
    for l in libs:
        startDate += l.signup_days
        if startDate > days:
            break
        l.sinupDate = startDate


    #Naive approach
    for d in range(days):
        for l in libs:
            checklib(l,explored_libs,d)
                    
                
