from recipe import Recipe
from ingredient import Ingredient

class MasterDB:

    def __init__(self, recipes, ingredients):
        self.recipes = recipes
        self.ingredients = ingredients

    def add_recipe(self, name, meal, ingrs, tags):
        rec = Recipe(name, meal, ingrs, tags)
        self.recipes.append(rec)

    def add_ingredient(self, name, cost, location, servings):
        self.ingredients.append(Ingredient(name, cost, location, servings))

    def get(self, list, id_list):
        return [x for x in list if x.id in id_list]

    def get_by_tags(self, tags):
        return [x for x in self.recipes if [t for t in x.tags if t in tags]]

    def get_by_meal(self, meals):
        return [x for x in self.recipes if x.meal in meals]

    def get_by_criteria(self, meal, tags):
        recs = []
        if meal and not tags:
            recs = (self.get_by_meal(meal))
        elif tags and not meal:
            recs = (self.get_by_tags(tags))
        elif meal and tags:
            list1 = (self.get_by_meal(meal))
            list2 = (self.get_by_tags(tags))
            recs = list(set(list1) & set(list2))
        else:
            recs = self.recipes

        return recs


    def find_ing_by_name(self, ingredient_name):
        for ing in self.ingredients:
            if ingredient_name == ing.name: return ing
        return False #if it hasn't returned the ingredient by now

    def find_rec_by_name(self, rec_name): 
        for rec in self.recipes:
            if rec_name == rec.name: return rec
        return False #if it hasn't returned the recipe by now

    def rec_cost_per_serving(self, rec):
        return sum(ingr.cost_per_serving() for ingr in self.get(self.ingredients, rec.ingredients))

    def rec_total_cost(self, rec):
        return sum(ingr.cost for ingr in self.get(self.ingredients, rec.ingredients))


    def edit_recipe_attr(self, rec_id, attribute, new_value):
        self.edit_attr(self.recipes, rec_id, attribute, new_value)

    def edit_ingr_attr(self, ingr_id, attribute, new_value):
        self.edit_attr(self.ingredients, ingr_id, attribute, new_value)

    def edit_attr(self, list, an_id, attribute, new_value):
        setattr(self.get(list, [an_id])[0] , attribute, new_value)


    def recipes_containing(self, list, ingr_id):
        return [rec for rec in list if ingr_id in rec.ingredients]

    def recipes_with_tag(self, list, tag):
        return [rec for rec in list if tag in rec.tags]   

    def remove_ingr_from_recipe(self, rec_id, ingr_id):
        for rec in self.recipes:
            if rec.id == rec_id:
                rec.ingredients = [ingr for ingr in rec.ingredients if ingr.id != ingr_id]

    def delete_ingredient(self, ingr_id):
        for ingr in self.ingredients:
            if ingr.id == ingr_id:
                self.ingredients.remove(ingr)
        for rec in self.recipes:
            self.remove_ingr_from_recipe(rec.id, ingr_id)
