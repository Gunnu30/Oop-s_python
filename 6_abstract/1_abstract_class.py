# Abstraction -> Hides implementation details, shows only essentials.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):   # must be implemented
        pass
    
    @abstractmethod
    def perimeter(self):   # must be implemented
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

# a = Shape()  # Error: abstract class can't be used directly


print('\n')
# Data abstraction using private object

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500

# print(account.__balance) # Error: can't access directly


print('\n')
# Public object

class A:
    def __init__(self,a):
        self.a = a     # public
obj1 = A(10)
print(obj1.a) # accessible


print('\n')
# Protected object

class Student:
    def __init__(self, name, age):
        self._name = name     # protected
        self._age = age       # protected

class Graduate(Student):
    def display(self):
        print("Name:", self._name)
        print("Age:", self._age)

g = Graduate("Bob", 25)
g.display()
print(g._name)   # accessible but discouraged

# meant for class + subclass only

print('\n')

# Getters , Setters 

class Student:
    def __init__(self, name):
        self.__name = name   # private object
    
    # Getter
    @property
    def name(self):             # getter returns the value
        return self.__name
    
    # Setter
    @name.setter
    def name(self, new_name):        # setters update and change the values.
        if len(new_name) > 1:   # simple validation
            self.__name = new_name
        else:
            print("Name too short!")

s = Student("Alice")
print(s.name)   # calls getter

s.name = "Bob"  # calls setter
print(s.name)

s.name = "A"    # validation fails
