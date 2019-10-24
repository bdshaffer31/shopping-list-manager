from recipe import Recipe
from ingredient import Ingredient
import itertools

class Book:
    newid = itertools.count().__next__
    
    def __init__(self, name, recipes):
        self.id = Book.newid()
        self.name = name
        self.recipes = recipes