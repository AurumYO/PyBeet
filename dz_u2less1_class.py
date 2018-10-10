class Person():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print("Hello, my name is", self.firstname, self.lastname, "and I'm", self.age, "years old.")

per1 = Person('Ivo', 'Bobul', 65)

per1.talk()