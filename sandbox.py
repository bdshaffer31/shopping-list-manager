from seeder import Seeder
from book_shelf import BookShelf
from confirm import confirm
import random
import datetime

#use function confirm() from confirm.py to check if user wants to proceed
if confirm("view recipe book contents")==False: 
    exit()

seeder = Seeder()
shelf = BookShelf() # empty book shelf to fill from seed
shelf = seeder.populate_bookshelf()

datetimeObj = datetime.datetime.today()
timestamp = datetimeObj.strftime("%d-%b-%Y (%H:%M:%S)") #.%f
print('Current Timestamp : ', timestamp)

breakfast = random.choice(shelf.master_list.find_recipes_by_meal('breakfast'))
print(breakfast.name)
daily_menu = shelf.create_ran_daily_rb()
for recipe in daily_menu.recipes:
    print(recipe.name)
    for ing in recipe.ingredients:
        print(ing.name)
for ing in daily_menu.ingredients:
    print(ing.name)

seeder.update_seed(shelf)