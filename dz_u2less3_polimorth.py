# Method overloading.
# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat,
# and make their own implementation of the method talk be different.
# For instance Dog’s can be to print ‘voff voff’, while Cat’s can be to print ‘meow’


class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')


class Dog(Animal):

    def talk(self):
        print(self.name + ' says - "Voff, voff, voooo"')


class Cat(Animal):

    def talk(self):
        print(self.name + ' says - "Meow, pfhhhh"')


cat1 = Cat('Betty')

dog2 = Dog('Goofy')

cat1.talk()
dog2.talk()
