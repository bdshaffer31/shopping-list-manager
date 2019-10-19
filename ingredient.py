class Ingredient:

    def __init__(self, name, cost, location, **kwargs):
        self.name = name
        self.cost = cost
        self.location = location
        self.servings = kwargs.get('servings', 1)

    def cost_per_serving(self):
        return float(self.cost) / float(self.servings)
