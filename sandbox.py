from seeder import Seeder
from book_shelf import BookShelf
from book import Book
from confirm import confirm
import random
import datetime

#use function confirm() from confirm.py to check if user wants to proceed
if confirm("view recipe book contents")==False: 
    exit()

shelf = BookShelf() # empty book shelf to fill from seed
shelf = shelf.populate_bookshelf()
shelf.update_pickle()

for rec in shelf.master_list.recipes:
    print(rec.name)


print('--------')

pickle_shelf = BookShelf()
pickle_shelf = pickle_shelf.populate_pickle()

for rec in pickle_shelf.master_list.recipes:
    print(rec.name)



shelf.update_seed()