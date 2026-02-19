#Hybris is a mix(multiple,hierarchial , multi-level), conbination of all.

# ---------MRO Order----------

#-> Start with the current class.

#-> Go left to right through base classes.

#-> Respect inheritance chains (parents before grandparents).

#-> No duplicates — each class appears only once.

#-> Always end with object (the ultimate base class in Python).

#EX:-2
            
            #   p
            #  / \
            # D   T

class Person:
    def introduce(self): 
        print("I am a person.")

# Hierarchical => P =>  T , D 
class Teacher(Person):
    def role(self):
        print("I teach.")

class Doctor(Person):
    def role(self):
        print("I heal.")

# Multilevel (Teacher → Professor)
class Professor(Teacher):
    def role(self):
        print("I guide research.")

# Multiple inheritance: Parent inherits from Doctor + Professor
class Parent(Doctor, Professor):
    def role(self):
        print("I balance teaching and healing.")



mom = Parent()
mom.introduce()
mom.role()

print(Parent.__mro__)
