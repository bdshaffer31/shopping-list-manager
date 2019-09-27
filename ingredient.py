class Ingredient:

    def __init__(self, name, cost, location, **kwargs):
        self.name = name
        self.cost = cost
        self.location = location
        self.servings = kwargs.get('servings', None)
