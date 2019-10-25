from recipe import Recipe
from ingredient import Ingredient
import itertools
from uuid import uuid4

class Book:
    newid = itertools.count().__next__

    def __init__(self, name, recipes):
        #self.id = Book.newid()
        self.id = uuid4().hex
        self.name = name
        self.recipes = recipes