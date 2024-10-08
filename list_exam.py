"""
QUESTIONS

- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals

"""

# SOLUTIONS

# ANSWER 1
zoo = ['Cat','Dog','Monkey','Parrot','Cow']

# ANSWER 2
third_animal = zoo.remove('Monkey')
print(f"Deleted the animal Monkey leaves my zoo with {third_animal }")

# ANSWER 3
append_animal = zoo.append('Lion')
print(f"Appended new animal to my list zoo = {append_animal }")

# ANSWER 4
delete_animal = zoo.pop(0)
print(f"Delete animal at index 0 of my zoo = {delete_animal}")

# ANSWER 5
print(f"Print my list of animals called zoo : {zoo}")

# ANSWER 6
only_first_3 = zoo[0:3]
print(f"Print only first 3  animals called : {only_first_3}")