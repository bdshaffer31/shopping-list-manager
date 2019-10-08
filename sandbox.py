from seeder import Seeder
from book_shelf import BookShelf
from book import Book
from confirm import confirm
from recipe import Recipe
import random
import datetime

shelf = BookShelf()
shelf = shelf.populate_bookshelf()

# for ingr in shelf.master_list.ingredients:
#     print(ingr.name + ' ' + str(len(ingr.name)))

# name = input('enter ingr name:')
# ingr = [ingr for ingr in shelf.master_list.ingredients if ingr.name == name]
# ingr = ingr[0]
# print(ingr.name)

rec = Recipe('soup','lunch',[])
check = hasattr(Recipe, 'tags')

print(check)
print(*rec.__dict__)
print(*rec.tags)

for rec in shelf.master_list.recipes:
    print(*rec.__dict__)
    rec = Recipe(rec.name, rec.meal, rec.ingredients)
    print(*rec.__dict__)
    print(*rec.tags)


shelf.update_db()
shelf = shelf.populate_bookshelf()
for rec in shelf.master_list.recipes:
    rec.tags = ['v']
    print(*rec.__dict__)

shelf.update_db()
    
shelf = shelf.populate_bookshelf()
for rec in shelf.master_list.recipes:

    print(*rec.__dict__)