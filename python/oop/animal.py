
class Animal:
    def __init__(self, animal_type, voice, legs):
        self.animal_type = animal_type
        self.voice = voice
        self.legs = legs
    def say_something(self):
        print(self.voice)
    def legs_qty(self):
        print(self.legs)

a1 = Animal("cat","miau", 4)
print(a1.animal_type)
print(a1.voice)
print(a1.legs)

a1.say_something()
a1.legs_qty()


