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

print(shelf.books[0].id)
#shelf.master_list.recipes = [x for x in shelf.master_list.recipes if x.name != 'test']
#shelf.update_db()