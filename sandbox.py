from book_shelf import BookShelf
from book import Book
from ingredient import Ingredient
from confirm import confirm
from recipe import Recipe
import random
import datetime
import mailer


message = 'hello ben'
rec = input('send list to what email? ')
mailer.send_email(message, rec)