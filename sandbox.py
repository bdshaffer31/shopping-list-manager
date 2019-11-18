from seeder import Seeder
from book_shelf import BookShelf
from book import Book
from ingredient import Ingredient
from confirm import confirm
from recipe import Recipe
import random
import datetime

shelf = BookShelf()
shelf = shelf.populate_bookshelf()

rec = shelf.master_list.find_rec_by_name('test rec')
ingr_ids = shelf.master_list.rec_ingrs(rec.id)
ingrs = shelf.master_list.get(shelf.master_list.ingredients, ingr_ids)
for ingr in ingrs:
    print(ingr.name)