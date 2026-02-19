#        Parent
#       /   |   \
#   Child1 Child2 Child3


# 'It is just like implementing single inheritance by more subclasses or children'
# this comment is enough no need to learn the code.

#Ex:- 1

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.greet()   # Inherited from Parent
obj2.greet()   # Inherited from Parent

print('\n')

#Ex:- 2
#overriding also.
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def greet(self):
        print("Hello from Child1")

class Child2(Parent):
    def greet(self):
        print("Hello from Child2")

obj1 = Child1()
obj2 = Child2()

obj1.greet()   # Child1 overrides parent
obj2.greet()   # Child2 overrides parent

print('\n')
# for mro view => c1 -> p and c2 -> p
print(Child1.__mro__)
print(Child2.__mro__)

print('\n')

#Ex:- 3
class Parent:
    def __init__(self):
        print("Parent __init__ called")

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("Child1 __init__ called")

class Child2(Parent):
    def __init__(self):
        super().__init__()
        print("Child2 __init__ called")

obj1 = Child1()
obj2 = Child2()
