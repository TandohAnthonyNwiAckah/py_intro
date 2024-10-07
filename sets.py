"""
 A set is an unordered collection data type that is mutable, iterable,
 and does not allow duplicate elements. Sets are commonly used for
 membership testing, removing duplicates from a sequence, and mathematical
 operations like union, intersection, and difference.

 Sets have unique values, unordered hence can’t be accessed with indexing

 Called with {}
"""

# Define a set with numbers from 1 to 15
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

# Print the set
print(f"Printing my set {my_set}")

# Union: Combines all unique elements from two sets.
setA = {1, 2, 3}
setB = {3, 4, 5}
union_set = setA | setB

print(f"Printing setA={setA} U SetA={setB} is  {union_set}")

# Intersection: Returns elements common to both sets.
intersection_set = setA & setB

print(f"Printing setA= {setA} n SetB ={setB} is  {intersection_set}")

# Difference: Returns elements in one(first set) set but not in the other.
difference_set = setA - setB

print(f"Printing setA ={setA} - SetB={setB} is  {difference_set}")


# Symmetric Difference: Returns elements that are in either of the sets but not in their intersection.
symmetric_difference_set = setA ^ setB

print(f"Printing setA ={setA} ^ SetB={setB} is {symmetric_difference_set}")


# Get the length of the set
setLength = len(my_set)
print(f"The length of my set is {setLength}")

# Loop through the set and print each element
for x in my_set:
    print(f"Looping through my set {x}")
    # print(f"{x}", end=' ')  # Use end=' ' to print elements on the same line, separated by a space

# remove() or discard(). Remove an element from the set using discard
my_set.discard(5)
print(f"My discard set is {my_set}")

# Remove all elements from the set
my_set.clear()
print(f"Clearing all element from my set {my_set}")

# Add an element back to the set
my_set.add(5)
print(f"Adding element back to my set{my_set}")

# Update the set by adding multiple elements
my_set.update([16, 17, 18])
print(f"Updating my set{my_set}")
