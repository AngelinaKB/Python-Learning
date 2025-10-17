# create a set
fruits = {"apple", "banana", "orange", "pear"}

# length of set
len(fruits)

# check membership
"apple" in fruits
"grapes" in fruits

# add elements
fruits.add("pineapple") # Used to add a single element to a set
fruits.update(["mango", "kiwi"]) # Used to add multiple elements (from any iterable) at once.

# remove elements
fruits.remove("apple")
fruits.discard("grapes")  # no error if element not found
fruits.pop()               # removes a random element

# copy and clear
copy_set = fruits.copy()
fruits.clear()

# frozen set example
frozen = frozenset(["apple", "banana", "cherry"]) # You can’t add, remove, or update elements.

