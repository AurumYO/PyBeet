# Create a class Person that has at least attributes first_name and last_name, use property decorators to create getters
# and setters for the email and fullname, email should be first_name.last_name@email.com and fullname just first_name
# together with last_name separated by a space character.


class Person:

    def __init__(self, first_name, last_name):
       self._first_name = first_name
       self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def email(self):
        self._email = self._first_name + '.' + self._last_name + "@email.com"
        return self._email

    @property
    def full_name(self):
        return self._first_name + " " + self._last_name


per1 = Person('Erykah', 'Badu')

print(per1.email)
print(per1.full_name)
per1.first_name = 'Joe'
print(per1.email)
per1.last_name = 'Doe'
print(per1.email)
print(per1.full_name)