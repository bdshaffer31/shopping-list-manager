from recipe import Recipe

proceed = input('search recipes/ (y/n): ')
if proceed == 'y':
    pass
elif proceed == 'n':
    exit()
else:
    print('please input y or n')
    exit()

seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx")

recipes = list()
for aline in seed_file:
    if len(aline) > 1:
        comps = aline.split(" | ")
        recipes.append(Recipe(comps[0],comps[1],comps[2]))

input_text = input('enter recipe name ')

for item in recipes:
    if item.name == input_text:
        print('found')
