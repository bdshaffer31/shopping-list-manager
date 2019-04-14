from recipe import Recipe
class RecipeBook:

    def __init__(self):
        self.recipes = []

    def populate_from_seed(self):
        #read the seed file
        seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx")
        #parse the seed file turning everything into recipes
        for aline in seed_file:
            if len(aline) > 1:
                comps = aline.split(" | ")
                self.recipes.append(Recipe(comps[0],comps[1],comps[2]))

    def write_in_seed(self):
        #get ready to write in seed file
        seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx", 'w')
        for item in self.recipes:
            seed_file.writelines(item.name + ' | ' + item.meal + ' | ' + item.ingredients + "\n")
        seed_file.close

    def add_recipe(self, name, meal, ingredients):
        self.recipes.append(Recipe(name, meal, ingredients))

