print("\n-> Over Riding Happens because of MRO! \n")
print("Example:- 1")
# Example 1: Base classes with no methods
class Base1:
    pass

class Base2:
    pass

# Subclass inheriting from both Base1 and Base2
class BothBase(Base1, Base2):
    # This print runs once when the class is defined (not when an object is created)
    print('\n')
    print("This is the Sub Class for both Super Classes")

# no use of 'BothBase()'
 
# obj creation and classing of Child class is not necessary.


print('\n')

# Example 2: Demonstrating MRO
class B1:
    pass

class B2:
    pass

class BothCls(B1, B2):
    print("Example:- 2 \n")
    def __init__(self):
        print("Method Resolution Order")

# Creating an object calls __init__, so this prints the message
obj1 = BothCls()

# __mro__ shows the order Python searches for methods:
# (BothCls, B1, B2, object)
print(BothCls.__mro__)

print('\n' , "Example:- 3 \n" )

# Example 3: Overriding with same method names
class Parent1:
    def greet(self):
        print("Hello from Parent1")

class Parent2:
    def greet(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    pass

obj = Child()
obj.greet()  # Which one runs? -> Parent1.greet()
print(Child.__mro__) 
# Python chooses Parent1.greet() first due to MRO order.

print('\n')

# Example 4: Child overriding parents directly
# Because of MRO Order first -> (Child, Parent1, Parent2, ...)

class Parent1:
    def greet(self):
        print("Hello from Parent1")

class Parent2:
    def greet(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    # Child overrides both parents by defining its own greet
    def greet(self):
        print("Hello from Child")

obj = Child()
obj.greet()   # Child's version wins
print(Child.__mro__)
