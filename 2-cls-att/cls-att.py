class Student:
    scl_name = "Rbs" # class attribute 

print(Student.scl_name)  # Rbs

s1 = Student()
s2 = Student()

print(s1.scl_name)       # Rbs
s1.scl_name = "Zphs"     # creates an instance attribute on s1 to store "Zphs"
print(s1.scl_name)       # Zphs
print(s2.scl_name)       # Rbs is not changed because s2 is still referring to the class attribute scl_name which is "Rbs"

Student.scl_name = "Bbs" # changes the class attribute scl_name = "Rbs" to "Bbs"

print(s1.scl_name)       # Zphs it come form s1 instance attribute
print(s2.scl_name)       # Bbs it come from class attribute scl_name which is changed to "Rbs" to "Bbs"


# how A class Attribute works with both instances.


class Student:
    total_students = 0  # Class Attribute (Static)

    def __init__(self, name):
        self.name = name  # Instance Attribute
        # Every time a new object is born, we update the CLASS variable
        Student.total_students += 1 

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name)            # Alice
print(s2.name)            # Bob
print(Student.total_students) # 2 (The Class remembers the total!)

#class attribute has only one memory location or copy for all the instances. so it give the same value to all the instances.
