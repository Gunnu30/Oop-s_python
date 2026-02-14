from abc import ABC , abstractmethod   # ABC  -> Abstract Base Class 

class Dad(ABC):
    @abstractmethod #-> @abstractmethod 
    def mainMtd(self):
        print("I am Abstract method which is declared in Abstract class.")

class Son(Dad):
    def mainMtd(self,a):
        print(a)

a = Son()
a.mainMtd(5)