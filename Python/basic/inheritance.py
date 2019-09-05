from Python.basic.Chef import Chef
from Python.basic.special_chef import SpecialChef


myChef = Chef()
myChef.make_special_dish()

mySpecialChef = SpecialChef()
mySpecialChef.make_special_dish()


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def miouh(self):
        print("miouh")


dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.miouh()

# By Victor Rybakovas Sep 2019 - http://bit.ly/linkedin-victor
