class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class Student(Person):

    def __init__(self, firstname, lastname, age, grade):
        super().__init__(firstname, lastname, age)
        self.grade = grade


class Teacher(Person):

    def __init__(self, firstname, midname, lastname, age, sallary):
        super().__init__(firstname, lastname, age)
        self.midname = midname
        self.sallary = sallary

s1 = Student('Ivo', 'Bobul', '16', 'A')
s2 = Student('Lilia', 'Sandulesa', '16', 'A')

s1 = Teacher('Maria', 'Petrivna','Sobko', '56', '4200')
