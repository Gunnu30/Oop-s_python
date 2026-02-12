class Bank:
    def __init__(self,acname,mobile,pin):
        self.acname=acname
        self.mobile=mobile
        self.__pin=pin
        self.__balance=10000
 
    def __shashi(self):
        upin=int(input("Arey Enter Pin: "))
        if upin==self.__pin:
            return True
        return False
    def balance(self):
        if self.__shashi():#True
            return f'Available balance is {self.__balance},\nEnjoy Fandagooo !'
        return f'Hey, You cant cheat me yaa , wrong ping'
 
    def withdrawl(self):
        if self.__shashi():#True
            uamount=int(input("Yentha kavali voi..."))
            if uamount<=self.__balance: #+ve account enough amount vundhi
                self.__balance-=uamount
                return f"Enjoy the amout, remainig is: {self.__balance}"
            else:
                return f'arey entra edhi, Insufficient funds:  {self.__balance}'
        else:
            return "you cant cheat me, wrong pin"
u1 = Bank("Gunnu" , 12345,2003)
print(u1.balance())