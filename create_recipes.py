from recipe_book import RecipeBook
from confirm import confirm

#use function confirm() from confirm.py to check if use wants to proceed
if confirm()==False: 
    exit()

book = RecipeBook()
book.populate_from_seed()

new_name = input('enter recipe name: ')
new_meal = input('enter recipe meal: ')
new_ingrediants = input('enter recipe ingrediants: ')

print(new_name)
print(new_meal)
print(new_ingrediants)

book.add_recipe(new_name, new_meal, new_ingrediants)
book.write_in_seed()