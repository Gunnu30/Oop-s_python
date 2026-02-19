# Normal Case

class ParClass:
    def __init__(self,name):
        self.name = name

class ChildCls(ParClass):
    pass
    # child doesn't have a constructor so it look up to the Parent class constructor.

obj1 = ChildCls("Ash")

print(obj1.name) # Ash -> The output Ash is Obtained from parent class not from Child.


# Error Case:

class ChildCls2(ParClass):
    def __init__(self):
        pass 

obj2 = ChildCls2("Sanju") # Error because child checks the constructor so it doesn't have argument but we are passing one Parameter. so it gives an error.


# How to Fix Case 2 Error:    using super().
class Parent:
    def __init__(self,name):
        self.name = name

class Child(Parent): # A Sub class or Child class inheritate by ClassName(Parent) syntax.

    def __init__(self,name,age):
        super().__init__(name) # super() is used to call the parent class's __init__ method to initialize the name attribute.
        self.age = age

c1 = Child("Ash" , 22)
print(c1.name) # Ash -> The output Ash is Obtained from parent class not from Child.
# Child has no name attribute so it looks up to the parent.

print(c1.age) # 22 -> The output is Obtained from child, because age is an attribute of child class.


# Method Overriding: Clearly explained in polymorphism folder.

class Parent1:
    def display(self):
        print("This is the Parent Class Method")

class Child1(Parent1):
    def display(self):
        print("This is the Child Class Method")

or1 = Child1()
or1.display() # Child class method display() is overriding the parent class method display().

#so the output is -> "This is the Child Class Method" 

# if we want to Call parent by child then 

class Parent2:
    def display(self):
        print("This is the Parent Class Method")

class Child2(Parent2):

    def display(self):
        super().display() # super() is used to call the parent class

or2 = Child2()
or2.display() # This is the Parent Class Methos 

# super() is recovered the Parent class methods which was overridden by the child.