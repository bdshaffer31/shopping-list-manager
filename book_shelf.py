from recipe_book import RecipeBook

class BookShelf:

    def __init__(self):
        self.master_list = RecipeBook("master", [], [])
        self.recipe_books = []
              
    def add_recipe_book(self, name, recipes, ingredients): #TODO add check if recipe already exists
        self.recipe_books.append(RecipeBook(name, recipes, ingredients)) 