from seeder import Seeder
from book_shelf import BookShelf
from confirm import confirm

# Hugely out of date, this needs to be handeled using seeder=>shelf=>book structure

#use function confirm() from confirm.py to check if user wants to proceed
if confirm("create new recipe")==False: 
    exit()

seeder = Seeder()
shelf = BookShelf() # empty book shelf to fill from seed
shelf = seeder.populate_bookshelf()

name = input('enter recipe name: ')
meal = input('enter recipe meal: ')
ingrediants = input('enter recipe ingrediants: ')

ingr_list = ingrediants.split(', ')

#check if ingredient sharing name exists
for ingr in ingr_list:
    found = False
    for item in shelf.master_list.ingredients:
        if ingr == item.name: found = True 
    if not found:
        print('new ingredient ' + ingr + ' enter additional info')
        cost = input('enter ingrediant cost: ')
        location = input('enter ingrediant location: ')
        shelf.master_list.add_ingredient(ingr, cost, location)

shelf.master_list.add_recipe(name, meal, ingr_list)
seeder.update_seed(shelf)