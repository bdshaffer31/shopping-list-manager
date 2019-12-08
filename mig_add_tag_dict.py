from seeder import Seeder
from book_shelf import BookShelf


shelf = BookShelf()
shelf = shelf.populate_bookshelf()

new_shelf = BookShelf()
new_shelf.master_list = shelf.master_list
new_shelf.books = shelf.books
print('done')

new_shelf.update_db()