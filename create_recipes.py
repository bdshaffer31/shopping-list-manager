from recipe import Recipe

proceed = input('create new recipe/ (y/n): ')
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

seed_file = open("C:/Users/Benjamin/Documents/RECIPE_APP/seed_file.tx", 'w')

new_name = input('enter recipe name: ')
new_meal = input('enter recipe meal: ')
new_ingrediants = input('enter recipe ingrediants: ')

print(new_name)
print(new_meal)
print(new_ingrediants)

recipes.append(Recipe(new_name, new_meal, new_ingrediants))

for item in recipes:
    seed_file.writelines(item.name + ' | ' + item.meal + ' | ' + item.ingredients + "\n")

seed_file.close