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
print('-gf/to-go-')
for rec in shelf.master_list.get_by_tags(shelf.master_list.recipes, ['gf','to-go']):
    print(rec.name)
print('-to-go-')
for rec in shelf.master_list.get_by_tags(shelf.master_list.recipes, ['to-go']):
    print(rec.name)
print('-v-')
for rec in shelf.master_list.get_by_tags(shelf.master_list.recipes, ['v']):
    print(rec.name)
