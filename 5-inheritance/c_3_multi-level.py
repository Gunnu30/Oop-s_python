print("Normal view -> GrandParent → Parent → Child") # inheritance chain
print("|")
print("MRO View -> Child → Parent → GrandParent → object") # actual search order

#Example:- 1
print('\n')
class GrandParent:
    def show(self):
        print("Hello from GrandParent")

class Parent(GrandParent):
    def show(self):
        print("Hello from Parent")

class Child(Parent):
    pass

obj = Child()
obj.show()   # Parent.show() runs
print(Child.__mro__) # Child → Parent → GrandParent → object

print('\n')

#Example:- 2

#Ex:- 2.1
class GrandP:
    def __init__(self):
        print("I am GrandParent")

class Pat1(GrandP):
    def __init__(self):
        print("I am Parent 1")

class Pat2(GrandP):
    def __init__(self):
        print("I am Parent 2")

class Chld(Pat1, Pat2):
    def __init__(self):
        print("I am Child")
        super().__init__()   # goes to Pat1 first (MRO order)

obj = Chld()  # Output: Child → Parent1

print('\n')

#Ex:- 2.2
class GrandEX2:
    def __init__(self):
        print("I am GrandParent")

class PatEX2_1(GrandEX2):
    def __init__(self):
        print("I am Parent 1")
        super().__init__()   # calls GrandParent

class PatEx2_2(GrandEX2):
    def __init__(self):
        print("I am Parent 2")

class ChldEx2(PatEX2_1, PatEx2_2):
    def __init__(self):
        print("I am Child")
        super().__init__()   # goes to Parent1, then GrandParent

obj = ChldEx2()  # Output: Child → Parent1 → GrandParent

print('\n')

#Ex:- 2.3

class GrandEX2:
    def __init__(self):
        print("I am GrandParent")

class PatEX2_1(GrandEX2):
    def __init__(self):
        print("I am Parent 1")
        super().__init__()

class PatEx2_2(GrandEX2):
    def __init__(self):
        print("I am Parent 2")
        super().__init__()

class ChldEx2(PatEX2_1, PatEx2_2):
    def __init__(self):
        print("I am Child")
        super().__init__()   # goes to Parent1 → Parent2 → GrandParent

obj = ChldEx2()  # Output: Child → Parent1 → Parent2 → GrandParent

print('\n')


# Example:- 4
#using super() before the child exection
class GrandParent:
    def __init__(self):
        print("GrandParent __init__ called")

class Parent(GrandParent):
    def __init__(self):
        super().__init__()   # ensures GrandParent runs
        print("Parent __init__ called")

class Child(Parent):
    def __init__(self):
        super().__init__()   # ensures Parent runs (which itself calls GrandParent)
        print("Child __init__ called")

obj = Child()

#Ex:- 5

# class G:
#     def __init__(self):
#         print("G")
# class P(G):
#     def __init__(self):
#         print("P")
# class c(P):
#     super().__init__() # super can't be used outsied of constructor __init__ 

print('\n')

#Ex:- 6

class Top:
    def greet(self):
        print("Hello from Base")

class Base(Top):
    def greet(self):
        # Call the parent's greet method
        super().greet()
        print("Hello from Derived")

obj = Base()
obj.greet()

print('\n')
