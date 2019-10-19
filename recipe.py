
class Recipe:

    def __init__(self, name, meal, ingredients, **kwargs):
        self.name = name
        self.meal = meal
        self.ingredients = ingredients
        self.tags = kwargs.get('tags', [])

    def cost_per_serving(self):
        return sum(ingr.cost_per_serving() for ingr in self.ingredients)

    def total_cost(self):
        return sum(ingr.cost for ingr in self.ingredients)