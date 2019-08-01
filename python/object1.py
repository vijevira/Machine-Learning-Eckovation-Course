class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        self.speed=0
    def increase_speed(self):
        self.speed+=10
    def decrease_speed(self):
        self.speed-=10

class BankAccount:
    def __init__(self,name):
        self.person=name
        self.balance=0
    def deposite(self,money):
        self.balance+=money
    def withdraw(self,money):
        if (money<=self.balance):
            self.balance-=money
        else:
            print("insufficient balance")
                

car1=Car("my car","black")
print(car1.name)
print(car1.color)
print(car1.speed)
ac=BankAccount("vijevira")
ac.deposite(10000)
ac.withdraw(4000)
