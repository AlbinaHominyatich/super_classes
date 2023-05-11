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

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'Name {self.name}, age {self.age}'
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def __str__(self):
        return super().__str__() + f" student_id {self.student_id} "
student1 = Student("Zahar", 45, "3264763t5812")

with open("info_student.txt", 'w') as file:
    file.write(str(student1))



