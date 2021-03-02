# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicles:
    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


vehicle_1 = Vehicles(180, 2000)
vehicle_2 = Vehicles(300, 1000000)

print(f'First car: speed {vehicle_1.max_speed} and mileage {vehicle_1.mileage}')
print(f'Second car: speed {vehicle_2.max_speed} and mileage {vehicle_2.mileage}')



# 2. Create a child class Bus that will inherit all of the variables and methods
# of the Vehicle class and will have seating_capacity own method

class Bus(Vehicles):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def define_seating_capacity(self):
        return self.seating_capacity


bus_1 = Bus(100, 0, "30 children")


print(f"First bus:  speed {bus_1.max_speed}, mileage {bus_1.mileage}, "
      f"and seating capacity", bus_1.define_seating_capacity())



# 3. Determine which class a given Bus object belongs to (Check type of an object)

print("Bus - ", type(Bus))


# 4. Determine if School_bus is also an instance of the Vehicle class

class School_Bus:
    pass


print(isinstance(School_Bus, Vehicles))



# # 5. Create a new class School with get_school_id and
# number_of_students instance attributes


class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        return self.school_id


school_1 = School(55, 150)
school_2 = School(1, 200)


print(f'First school: id -',  school_1.get_school_id(),
      f', number of students - {school_1.number_of_students}')
print(f'Second school: id -', school_2.get_school_id(),
      f', number of students - {school_2.number_of_students}')



# 6*. Create a new class SchoolBus that will inherit
# all of the methods from School and Bus and will have its own - bus_school_color


class SchoolBus(School, Bus):
    def __init__(self, max_speed=100, mileage=1000, seating_capacity="20 children",
                 school_id=1, number_of_students=500, bus_school_color="Yellow"):
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        School.__init__(self, school_id, number_of_students)
        self.bus_school_color = bus_school_color


school_bus = SchoolBus()


print(f'The school bus: max speed - {school_bus.max_speed}, mileage - {school_bus.mileage}, '
      f'seating capacity - {school_bus.seating_capacity}, id -', school_bus.get_school_id(),
      f'number of students - {school_bus.number_of_students}, color - {school_bus.bus_school_color}')



# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:
    def make_sound(self):
        print('Bears roar')


class Wolf:
    def make_sound(self):
        print('Wolves bark')


bear = Bear()
wolf = Wolf()

animals = (bear, wolf)

for animals in (bear, wolf):
    animals.make_sound()



# 8. Create class City with name, population instance attributes,
# return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
# 9. Override a printable string representation of the City class
# and return: The population of the city {name} is {population}


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            print("Your city is too small")

    def __str__(self):
        return f'The population of {self.name} is {self.population}.'


city_1 = City("Zhmerynka", 896)
city_2 = City("Antananarivo", 1275207)

print(city_1)
print(city_2)



# 10*. Override magic method __add__() to perform the additional action
# as 'multiply' (*) the value which is greater than 10.
# And perform this add (+) of two instances.


class Addition:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if self.value > 10 or other.value > 10:
            return self.value * other.value
        return self.value + other.value


addition_1 = Addition(99)
addition_2 = Addition(7)
sum = addition_1 + addition_2

print(f'The result is', sum)



# 11. The __call__ method enables Python programmers to write classes
# where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class Sum:
    def __call__(self, number_1, number_2):
        return number_1 + number_2


sum_1 = Sum()
print("The sum is", sum_1(22, 17))



# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy
# if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) == 0:
            return False
        return True


order_1 = MyOrder(["Burger", "Salad"], "Kiki")
order_2 = MyOrder([], "Pepa")

print(bool(order_1))
print(bool(order_2))
