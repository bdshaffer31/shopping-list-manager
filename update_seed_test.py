from seeder import Seeder
from book_shelf import BookShelf
from confirm import confirm

#use function confirm() from confirm.py to check if user wants to proceed
if confirm("view recipe book contents")==False: 
    exit()

seeder = Seeder()
shelf = BookShelf() # empty book shelf to fill from seed
shelf = seeder.populate_bookshelf()

seeder.update_seed(shelf)