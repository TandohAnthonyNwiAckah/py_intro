"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values

"""


# SOLUTION
def namer(firstname, lastname, age):
    dict_name = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return dict_name


result = namer('TANACOM', 'IO', '5')
print(result)
