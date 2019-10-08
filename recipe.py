
class Recipe:

    def __init__(self, name, meal, ingredients, **kwargs):
        self.name = name
        self.meal = meal
        self.ingredients = ingredients
        self.tags = kwargs.get('tags', [])
