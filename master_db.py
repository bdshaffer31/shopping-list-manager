from recipe import Recipe
from ingredient import Ingredient

class MasterDB:

    def __init__(self, recipes, ingredients):
        self.recipes = recipes
        self.ingredients = ingredients

    def get_ingr(self, ingr_id):
        return self.get(self.ingredients, ingr_id)

    def get_rec(self, rec_id):
        return self.get(self.recipes, rec_id)

    def get(self, list, an_id):
        return [x for x in list if x.id == an_id][0]

    def find_ing_by_name(self, ingredient_name): # this was changed and that broke some things 
        for ing in self.ingredients:
            if ingredient_name == ing.name: return ing
        return False #if it hasn't returned the ingredient by now

    def find_rec_by_name(self, rec_name): # this was changed and that broke some things 
        for rec in self.recipes:
            if rec_name == rec.name: return rec
        return False #if it hasn't returned the ingredient by now

    def find_recipes_by_meal(self, meal): 
        recipe_list = [x for x in self.recipes if x.meal == meal]
        return recipe_list

    def get_ingrs_from_ids(self, ingr_ids):
        ingredients = [x for x in self.ingredients if x.id in ingr_ids]
        return ingredients  

    def rec_cost_per_serving(self, rec):
        return sum(ingr.cost_per_serving() for ingr in self.get_ingrs_from_ids(rec.ingredients))

    def rec_total_cost(self, rec):
        return sum(ingr.cost for ingr in self.get_ingrs_from_ids(rec.ingredients))

    def edit_recipe_attr(self, rec_id, attribute, new_value):
        self.edit_attr(self.recipes, rec_id, attribute, new_value)

    def edit_ingr_attr(self, ingr_id, attribute, new_value):
        self.edit_attr(self.ingredients, ingr_id, attribute, new_value)

    def edit_attr(self, list, an_id, attribute, new_value):
        setattr(self.get(list, an_id) , attribute, new_value)


    def all_recs_containing(self, ingr_id):
        self.recipes_containing(self.recipes, ingr_id)

    def recipes_containing(self, list, ingr_id):
        pass

    def all_recs_with_tag(self, tag):
        self.recipes_with_tag(self.recipes, tag)

    def recipes_with_tag(self, list, tag):
        pass   

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
