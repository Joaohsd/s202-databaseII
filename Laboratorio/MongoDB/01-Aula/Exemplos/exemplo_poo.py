class Dog:
    __tipo = "Yorkshire"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, volume):
        print("The dog " + self.name + " is barking so " + volume + "!")

dog = Dog("Dog1", 1)

print(dog.name)
print(dog.age)
print(dog.__tipo)

dog.bark("low")

class Big_Dog(Dog):
    def bark(self):
        print("The dog " + self.name + " is barking so high!")

dog2 = Big_Dog('Dog2', 2)

print(dog2.name)
print(dog2.age)
print(dog2.__tipo)

dog2.bark()
