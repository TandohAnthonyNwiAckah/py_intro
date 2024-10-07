"""
Lists are arrays and allow indexing, insert and updates

 Called with []
"""

# Initialize a list with elements
my_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Access and print the first element of the list (index 0)
print(f"The first element of my list is {my_list[0]}")

# Calculate and print the sum of all elements in the list
print(f"The sum of all element in my list is {sum(my_list)}")

# Get and print the length of the list (number of elements)
print(f"The length of my list is {len(my_list)}")

# Slice and print the first two elements of the list (from index 0 up to, but not including, index 2)
print(f"The first two element of my list is {my_list[0:2]}")

# Append a new element (100) at the end of the list
my_list.append(100)
print(f"Appending 100 to my list {my_list}")

# Insert a new element (2000) at index 2, shifting other elements to the right
my_list.insert(2, 2000)
print(f"Inserting element at index 2 of my list {my_list}")

# Remove the first occurrence of the value 2 from the list
my_list.remove(2)
print(f"Removing value 2 from my list {my_list}")

# Remove and return the element at index 2, and print the updated list
my_list.pop(2)
print(f"Removing element at index 2 {my_list}")

# Sort the list in ascending order (modifies the list in place)
my_list.sort()
print(f"Sorting my list {my_list}")
