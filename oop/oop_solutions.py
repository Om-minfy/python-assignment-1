# Easy Questions
# 1. Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

print("Rectangle:")
r = Rectangle(5, 10)
print("Area:", r.area())
print("Perimeter:", r.perimeter())


# 2. Counter class
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def reset(self):
        self.value = 0

print("\nCounter:")
c = Counter()
c.increment()
c.increment()
print("Value:", c.value)
c.decrement()
print("Value:", c.value)
c.reset()
print("Value:", c.value)


# Medium Questions
# 3. Vehicle and Car
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel = fuel

print("\nCar:")
car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print("Make:", car.make)
print("Doors:", car.doors)


# 4. BankAccount (with private variables)
class BankAccount:
    def __init__(self, acc_no, balance):
        self.__acc_no = acc_no
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__acc_no

print("\nBank Account:")
acc = BankAccount("123456", 1000)
print("Balance:", acc.get_balance())
acc.deposit(500)
print("Balance:", acc.get_balance())
acc.withdraw(200)
print("Balance:", acc.get_balance())
print("Account No:", acc.get_account_number())

try:
    acc._balance = 2000
except AttributeError:
    print("Cannot directly access private attribute")