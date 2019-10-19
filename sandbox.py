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

b = Ingredient('banana', '0.70', 'produce', servings = '6')
print(b.cost_per_serving())

print(shelf.master_list.recipes[11].cost_per_serving())
print((shelf.master_list.recipes[11]).name)