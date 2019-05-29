class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")


    def eat(self):
        print("I am eating  meat")

    def bark(self):
        print("Woof!")


my_animal = Dog()
print(my_animal.who_am_i())
