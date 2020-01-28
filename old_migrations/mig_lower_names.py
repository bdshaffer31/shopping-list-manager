from book_shelf import BookShelf

shelf = BookShelf()
shelf = shelf.populate_bookshelf()

for recipe in shelf.master_list.recipes:
    recipe.name = recipe.name.lower()

for ingr in shelf.master_list.ingredients:
    ingr.name = ingr.name.lower()

print('done')

shelf.update_db()

