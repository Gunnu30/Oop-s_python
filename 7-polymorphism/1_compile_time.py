#Compile-time polymorphism (method overloading) 
# is not built-in, 
# but you can simulate it with flexible argument handling.


class Demo:
    def greet(self, name=None, age=None):
        if name and age:
            print(f"Hello {name}, you are {age} years old")
        elif name:
            print(f"Hello {name}")
        else:
            print("Hello, World")

obj = Demo()
obj.greet()              # Hello, World
obj.greet("Ashrith")     # Hello Ashrith
obj.greet("Ashrith", 21) # Hello Ashrith, you are 21 years old
