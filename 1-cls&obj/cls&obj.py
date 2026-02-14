# 1. THE CLASS (The Blueprint)
class MyClass:
    def __init__(self):
        # This runs the moment an object is "born"
        print("A new object was created!")

# 2. THE OBJECT (The Instance)
# We use the class name followed by () to 'call' the blueprint into action.
obj1 = MyClass() 
obj2 = MyClass() 

# 3. THE IDENTITY (Where it lives)
print(obj1) # Shows the type and the unique Memory Address



                    # About self operations.

class Car:
    def __init__(self,brand,model): # self is a reference to the current instance or object 
        self.brand = brand # atributes
        self.model = model

c1 = Car("Toyota","Comry") # self allocates memory for this object

c2 = Car("Honda","Civic") # self allocates memory for this object

print(c1.brand) # self knows to give from which object to get the values.