vegetables = ["celery", "carrots", "potatoes"]
meats =      ("chicken", "fish", "turkey")

groceries = [["apple", "orange", "banana", "coconut"], vegetables, meats]

print(groceries[0]) # first index => entire list
print(groceries[0][3]) # first element of the first index list

# Iterate over elements of 2d list

for collection in groceries:
  print(collection)
  
# to iterate over elements inside each list
for collection in groceries:
  for food in collection:
    print(food, end=" ")
  print()
