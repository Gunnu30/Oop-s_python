class Student:
    def __init__(self, name):
        self.name = name  # Instance attribute created here

    def change_name(self, new_name):   # method way
        self.name = new_name

s1 = Student("Ash")
s2 = Student("Sanju")

# Way 1: using method
s1.change_name("Gunnu")
print(s1.name)   # Gunnu

print(s2.name)   # Sanju (unchanged) because we changed only s1's name, s2 will be unaffected.


# Way 2: direct assignment
s1.name = "bb"
print(s1.name)   # bb

print(s2.name)   # Sanju (unchanged)