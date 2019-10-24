import itertools

class Ingredient:
    newid = itertools.count().__next__

    def __init__(self, name, cost, location, servings):
        self.id = Ingredient.newid()
        self.name = name
        self.cost = cost
        self.location = location
        self.servings = servings

    def cost_per_serving(self):
        return float(self.cost) / float(self.servings)
