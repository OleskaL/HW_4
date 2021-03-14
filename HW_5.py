# 1.
class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self, laptop_manufacturer, hours_of_work):
        self.laptop_manufacturer = laptop_manufacturer
        self.battery = Battery(hours_of_work)

    def __str__(self):
        return f'{self.battery}'

class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, hours_of_work):
        self.hours_of_work = hours_of_work

    def __str__(self):
        return f'{self.hours_of_work}'


laptop_1 = Laptop("Apple", 7)

print(f'The laptop manufacturer is {laptop_1.laptop_manufacturer}, '
      f'and battery working hours are', laptop_1)


# 2.
class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, name, string):
        self.name = name
        self.string = string


class GuitarString:
    """
    Make the class with aggregation
    """
    def __init__(self, string_length):
        self.string_length = string_length


string = GuitarString(4)
guitar = Guitar("Lennon", string.string_length)

print(f'{guitar.name}, {guitar.string}')


# 3
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters,
    which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """
    @staticmethod
    def add_nums(x, y, z):
        return x+y+z


print(Calc.add_nums(5, 3, 8))


# 4
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients
    and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    CARBONARA = ['forcemeat', 'tomatoes']
    BOLOGNAISE = ['bacon', 'parmesan', 'eggs']

    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients


    @classmethod
    def carbonara(cls):
        return Pasta(cls.CARBONARA)

    @classmethod
    def bolognaise(cls):
        return Pasta(cls.BOLOGNAISE)


pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()
pasta_3 = Pasta.carbonara()

print(pasta_1.list_of_ingredients)
print(pasta_2.list_of_ingredients)
print(pasta_3.list_of_ingredients)


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and
    its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num -
    visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """

    max_visitors_num = 22

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, x):
        if x < self.max_visitors_num:
            self._visitors_count = x
        else:
            self._visitors_count = self.max_visitors_num


Concert.max_visitor_num = 50
concert = Concert(50)
concert.visitors_count = 1000
print(concert.visitors_count)


#6.
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str),
    phone_number (str), address (str), email (str), birthday (str), age (int)
    """

    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


contact_1 = AddressBookDataClass(1, 'Kiki', '8758181', 'City',
                                 'jahjsHJAH@gmail.com', '11.09.1919', 101)
print(contact_1.address)


# 7. Create the same class (6) but using NamedTuple
import collections


AddressBookDataClass_1 = collections.namedtuple('AddressBookDataClass_1',
                                                ['key', 'name', 'phone_number', 'address',
                                                 'email', 'birthday', 'age'])

contact_1 = AddressBookDataClass_1(1, 'Kiki', '8758181', 'City',
                                   'jahjsHJAH@gmail.com', '11.09.1919', 101)

print(contact_1[2])


# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address,
    email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'{AddressBook}, {self.key}, {self.name}, {self.phone_number}, {self.address}, ' \
               f'{self.email}, {self.birthday}, {self.age}'


contact_2 = AddressBook(key=1, name='Pedro', phone_number='1717171', address='Tokyo',
                        email='jahsgd@gmail.com', birthday='17.08.2004', age=16)
print(contact_2.name)


# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person_1 = Person()

setattr(person_1, 'age', '77')
# print(getattr(person_1, 'name', 'age'))

print(f'{person_1.name} is {person_1.age}.')


# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student_1 = Student(1, "Kiki")
setattr(student_1, "email", "student@gmail.com")
print(getattr(student_1, "email"))


#11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def convert(self):
        return (self._temperature * 1.8) + 32


cels_fahr = Celsius(5)

print(cels_fahr.convert)
