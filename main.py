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
