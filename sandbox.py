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

print(*shelf.master_list.ingredients[3].__dict__)
print((shelf.master_list.ingredients[3]).id)

print(shelf.master_list.recipes[11])
print((shelf.master_list.recipes[11]).name)
print((shelf.master_list.recipes[11]).ingredients)

print('----')
print((shelf.books[2]).recipes)
