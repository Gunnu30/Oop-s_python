class Student:
    def __init__(self, name):
        self.name = name   # instance attribute

    def change_name(self, new_name):   # method way
        self.name = new_name

s1 = Student("Ash")
s2 = Student("Sanju")

# Way 1: using method
s1.change_name("Changed")
print(s1.name)   # Changed

# Way 2: direct assignment
s1.name = "bb"
print(s1.name)   # bb

print(s2.name)   # Sanju (unchanged)