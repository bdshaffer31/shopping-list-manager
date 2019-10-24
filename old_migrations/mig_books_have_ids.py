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

all_books = []

for book in shelf.books:
    #print(recipe.ingredients)
    rec_ids = []
    for rec in book.recipes:
        for master_rec in shelf.master_list.recipes:
            if rec == master_rec.name:
                rec_ids.append(master_rec.id)
        
    all_books.append(Book(book.name, rec_ids))
    #print(recipe.ingredients)

shelf.books = all_books
print('done')

shelf.update_db()