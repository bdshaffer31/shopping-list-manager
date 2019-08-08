# test script to figure out how to use list comprehension to properly read recipes
line = " tomato,  rice, orange juice, ,beans,, ,"
print(line)
raw_list = line.split(",")
print(raw_list)
striped_list = [item.strip() for item in raw_list]
print(striped_list)
filtered_list = [item for item in striped_list if item]
print(filtered_list)
combined_list = [item.strip() for item in raw_list if item.strip()]
print(combined_list)