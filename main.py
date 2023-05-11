class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name, "кушає")
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def bark(self):
        print(self.name, 'гавкає')
hotdog = Dog("bobik", 3, 'labrodor')
print(hotdog.name, hotdog.breed, hotdog.age)
hotdog.eat()

import random

class Animal:
    def __init__(self, species, name, age, health, hunger, happiness):
        super().__init__()
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
    def grow(self):
        self.age += 1
        self.health = random.randint(0, 10)
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(0, 10)
    def eat(self):
        if self.hunger >= 6:
            self.health += random.randint(0, 5)
            self.happiness += random.randint(0, 5)
            self.hunger -= random.randint(5, 7)
        else:
            print(self.name, " голодний")
    def play(self):
        pass #happiness
class Zoo:
    def __init__(self):
        super().__init__()
        self.animals = []