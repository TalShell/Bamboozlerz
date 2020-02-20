#! /usr/bin/env python3

from library import Library
from book import Book

def process(books, libs, days):
    explored_libs=[]
    startDate=0;
    for l in libs:
        startDate += l.signup_days
        l.sinupDate = startDate
    
    for d in range(days):
        for l in libs:
            for bk in libs.unique_books:
                if not bk.is_scanned:
                    bk.is_scanned=True
                    explored_libs.append(l)
                    
    for l in libs:
        for bk in libs.unique_books:
            if bk.is_scanned:
                print(l,bk)
    
