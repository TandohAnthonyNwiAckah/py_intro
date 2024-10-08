# Python Object-Oriented Programming (OOP)

## Overview
Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to design software. OOP concepts like **Abstraction**, **Inheritance**, **Encapsulation**, and **Polymorphism** help in structuring programs, making them more modular, reusable, and easier to maintain.

## Table of Contents
1. [Classes and Objects](#classes-and-objects)
2. [Abstraction](#abstraction)
3. [Inheritance](#inheritance)
4. [Encapsulation](#encapsulation)
5. [Polymorphism](#polymorphism)
6. [Self vs Super](#self-vs-super)
7. [Conclusion](#conclusion)

## Classes and Objects

- **Class**: A blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class can have.
- **Object**: An instance of a class. It contains attributes (data) and methods (functions) defined in the class.

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes a {self.sound} sound."

```

## Abstraction
- Abstraction hides the complex implementation details
and shows only the essential features of an object. 
It is achieved using abstract classes and interfaces
in Python.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)


```

- **Abstract Base Class** : Cannot be instantiated and typically contains one or more abstract methods that subclasses must implement.

## Inheritance
- Inheritance allows a class to inherit attributes and methods from another class. It supports code reusability and establishes a relationship between parent and child classes.

```python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."


```
- Parent Class: The class being inherited from.
- Child Class: The class that inherits from another class.


## Encapsulation
- Encapsulation restricts access to the internal state of an object. It is done using access specifiers:

- **Public**: Accessible anywhere.
- **Protected**: Prefixed with a single underscore (_) and should not be accessed outside the class hierarchy.
- **Private** : Prefixed with double underscores (__) and cannot be accessed outside the class directly.


```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount


```


## Polymorphism
Polymorphism allows objects of different classes to be
treated as objects of a common super class. It can be 
achieved through method overriding and method overloading.




```python

class Bird:
    def speak(self):
        return "Bird is singing."

class Sparrow(Bird):
    def speak(self):
        return "Sparrow is chirping."

def make_sound(bird: Bird):
    print(bird.speak())

# Different objects respond to the same function call
make_sound(Bird())    # Output: Bird is singing.
make_sound(Sparrow()) # Output: Sparrow is chirping.


```


## Self vs Super
- **self** : Refers to the instance of the class. 
It is used to access instance variables and methods.


```python
class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"{self.name} has a maximum speed of {self.max_speed} km/h.")


```


- **super()** : Refers to the parent class and is used to access parent class methods and attributes.

```python
class Car(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed)
        self.mileage = mileage

    def display(self):
        super().display()
        print(f"{self.name} has a mileage of {self.mileage} km/l.")


```


## Conclusion
- Object-Oriented Programming in Python provides a clear modular structure for programs. By understanding and implementing OOP concepts like Abstraction, Inheritance, Encapsulation, and Polymorphism, you can build scalable and maintainable applications.