"""
Tuples in Python are immutable data structures,
 meaning that once they are created, you cannot modify, add, or remove elements.

 Tuples are immutable once set

 Called with ()
"""

# Define a tuple with elements.
my_tuple = (1, 2, 3, 4, 5)

# Print the contents of the tuple.
print("Original tuple:", my_tuple)

# Uncommenting the line below will raise an error, because tuples are immutable.
# my_tuple[0] = 10  # Error: TypeError: 'tuple' object does not support item assignment

# Example 1: Accessing elements in a tuple using indexing
first_element = my_tuple[0]  # Access the first element, which is 1
print("First element of the tuple:", first_element)

# Example 2: Slicing a tuple
sliced_tuple = my_tuple[1:3]  # Slice the tuple from index 1 to 3
print("Sliced tuple (index 1 to 3):", sliced_tuple)

# Example 3: Iterating through a tuple
print("Iterating through the tuple:")
for item in my_tuple:
    print(item)

# Example 4: Concatenating two tuples
new_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + new_tuple
print("Concatenated tuple:", concatenated_tuple)

# Example 5: Checking if an element exists in a tuple
is_present = 3 in my_tuple
print("Is 3 present in my_tuple?", is_present)

# Example 6: Getting the length of a tuple
length_of_tuple = len(my_tuple)
print("Length of my_tuple:", length_of_tuple)

# Example 7: Nesting tuples (a tuple inside another tuple)
nested_tuple = (my_tuple, new_tuple)
print("Nested tuple:", nested_tuple)

# Example 8: Unpacking tuple elements into variables
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)


