from recipe_book import RecipeBook
from confirm import confirm

#use function confirm() from confirm.py to check if user wants to proceed
if confirm("view recipe book contents")==False: 
    exit()

book = RecipeBook()
book.populate_from_seed()

for rec in book.recipes:
    print("- " + rec.name + " - ", end = " ")
    for ing in rec.ingredients:
        print(ing + ", ", end = " ")
    print()
