class Student:
    school_name = "ABC School"   # class attribute

    def __init__(self, name):
        self.name = name         # instance attribute

    # Instance method → works with object data
    def show_info(self):
        print(f"{self.name} studies at {self.school_name}")

    # Class method → works with class data
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Static method → utility, no self/cls
    @staticmethod
    def greet():
        print("Hello Students!")

    @staticmethod
    def custom_greet(name, school):
        print(f"{name} studies at {school}")


# Usage
s1 = Student("Ash")
s2 = Student("Sanju")

# Instance methods
s1.show_info()       # Ash studies at ABC School
s2.show_info()       # Sanju studies at ABC School

# Class method
Student.change_school("XYZ School")
s1.show_info()       # Ash studies at XYZ School
s2.show_info()       # Sanju studies at XYZ School

# Static methods
Student.greet()      # Hello Students!
Student.custom_greet(s1.name, Student.school_name)  # Output: Ash studies at XYZ School

s1.greet() # static methods can be utilized with obj also.
