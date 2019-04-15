from recipe_book import RecipeBook
from confirm import confirm

#use function confirm() from confirm.py to check if use wants to proceed
if confirm()==False: 
    exit()

book = RecipeBook()
book.populate_from_seed()

name = input('enter recipe name: ')
meal = input('enter recipe meal: ')
ingrediants = input('enter recipe ingrediants: ')

ingr_list = ingrediants.split(', ')

#check if ingredient sharing name exists
for ingr in ingr_list:
    found = False
    for item in book.ingredients:
        if ingr == item.name: found = True 
    if not found:
        print('new ingredient ' + ingr + ' enter additional info')
        cost = input('enter ingrediant cost: ')
        location = input('enter ingrediant location: ')
        book.add_ingredient(ingr, cost, location)

book.add_recipe(name, meal, ingr_list)
book.update_seed()