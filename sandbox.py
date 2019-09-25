from seeder import Seeder
from book_shelf import BookShelf
from book import Book
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

print('------')
book1 = Book('test_book', ['pb&j', 'oatmeal', 'lasagna'])
ingr_list = shelf.book_ingr_list(book1)
#print(*ingr_list, sep = ', ')
ingr_list = shelf.shopping_list(ingr_list)
for ingr in ingr_list:
    print(ingr.name)

seeder.update_seed(shelf)