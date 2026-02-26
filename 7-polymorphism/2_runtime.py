# Polymorphism means many forms.

#Same method name but Different Parameters
 

#Ex:- 1

class A:
    def speed(self):
        print("I am A Speed")
class B(A):
    def speed(self): # This method overrids A class medthod (speed).
        print("I am B speed")

oj1 = B()
oj1.speed()# Here -> I am B speed

print("\n")

#Ex:- 2

# Parrent class methods is trying to override Child Class.

class Parent:
    def poet(self):
        print("I am a Parent-> Poet")
class Child(Parent):
    def poet(self):
        super().poet()
obj = Child()
obj.poet() 

obj1 = Parent() # This is not Overriding, just a method accessing
obj1.poet()