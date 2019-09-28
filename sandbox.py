from seeder import Seeder
from book_shelf import BookShelf
from book import Book
from confirm import confirm
import random
import datetime

shelf = BookShelf()
shelf = shelf.populate_bookshelf()

for ingr in shelf.master_list.ingredients:
    print(ingr.name + ' ' + str(len(ingr.name)))

name = input('enter ingr name:')
ingr = [ingr for ingr in shelf.master_list.ingredients if ingr.name == name]
ingr = ingr[0]
print(ingr.name)