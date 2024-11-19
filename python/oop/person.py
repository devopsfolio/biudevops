
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


p1 = Person("Andrey", 30)

print(p1.age)

p1.birthday()

print(p1.age)


