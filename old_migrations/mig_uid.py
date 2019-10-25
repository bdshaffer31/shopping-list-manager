from seeder import Seeder
from book_shelf import BookShelf
from book import Book
from ingredient import Ingredient
from confirm import confirm
from recipe import Recipe
import random
import datetime

ing_id_to_uid = []
rec_id_to_uid = []

shelf = BookShelf()
shelf = shelf.populate_bookshelf()

all_ingr = []
print(' --Ingredients-- ')
for ingr in shelf.master_list.ingredients:
    new_ingr = Ingredient(ingr.name, ingr.cost, ingr.location, ingr.servings)
    print(ingr.id)
    print(new_ingr.id)
    all_ingr.append(new_ingr)
    ing_id_to_uid.append((ingr.id, new_ingr.id))
    
print(all_ingr)
shelf.master_list.ingredients = all_ingr

print(ing_id_to_uid)

all_recipe = []
print(' --Recipes-- ')
for recipe in shelf.master_list.recipes:
    ingrs = []
    for ingr in recipe.ingredients:
        for tup in ing_id_to_uid:
            if tup[0] == ingr:
                ingrs.append(tup[1])
    print(recipe.ingredients)
    print(ingrs)
    new_rec = Recipe(recipe.name, recipe.meal, ingrs, recipe.tags)
    print(recipe.id)
    print(new_rec.id)
    all_recipe.append(new_rec)
    rec_id_to_uid.append((recipe.id, new_rec.id))

print(all_recipe)
shelf.master_list.recipes = all_recipe

print(rec_id_to_uid)

all_books = []
print(' --Books-- ')
for book in shelf.books:
    recs = []
    for rec in book.recipes:
        for tup in rec_id_to_uid:
            if tup[0] == rec:
                recs.append(tup[1])
    print(book.recipes)
    print(recs)
    new_book = Book(book.name, recs)
    print(book.id)
    print(new_book.id)
    all_books.append(new_book)

print(all_books)
shelf.books = all_books

shelf.update_db()

shelf = shelf.populate_bookshelf()
shelf.update_db()