"""
Dictionary in Python: A dictionary is a collection of key-value pairs.
 Each key in a dictionary must be unique and immutable,
 while the values can be of any data type.
Dictionaries are unordered, meaning they don't keep
the order of elements as they were added.

Below is a demonstration of dictionary operations in Python:
"""

my_dictionary = {
    'name': 'tanacom',
    'country': 'ghana'
}

# Print the entire dictionary
print(f"Printing all my dictionary: {my_dictionary}")

# Accessing a value using a key
print(f"Printing the value for the key 'name': {my_dictionary['name']}")

# Adding a new key-value pair to the dictionary
my_dictionary['city'] = 'Accra'
print(f"Added a new item to my dictionary: {my_dictionary}")

# Printing the length of the dictionary
print(f"Length of my dictionary is: {len(my_dictionary)}")

# Looping through the dictionary and printing keys and values
print(f"Printing key and values in my dictionary")
for key, value in my_dictionary.items():
    print(f" {key} : {value}")

# Popping a key-value pair from the dictionary
popped_item = my_dictionary.pop('city')
print(f"Popped item is: {popped_item}")

# Clearing all items from the dictionary
my_dictionary.clear()
print(f"My dictionary after clearing: {my_dictionary}")
