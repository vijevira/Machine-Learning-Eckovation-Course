class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def add(self,complex_no):
        self.real+=complex_no.real
        self.imag+=complex_no.imag
    def subtract(self,complex_no):
        self.real-=complex_no.real
        self.imag-=complex_no.imag
    def __str__(self):
        return (str(self.real)+"+i("+str(self.imag)+")")

class Employee:
    def __init__(self,name,salary,isSenior):
        self.name=name
        self.salary=salary
        self.isSenior=isSenior
    def amIaSenior(self):
        if(self.isSenior):
            print("senior")
        else:
            print("junior")

class Television:
    def __init__(self):
        self.state="off"
        self.volume=0
        self.channel=0
    def change_channel(self,number):
        self.channel=number
    def increase_volume(self,volume):
        self.volume+=volume

    def toggle_tv(self):
        if self.state=="off":
            self.state="on"
        else:
            self.state="off"
        
c1=ComplexNumber(3,6)
c2=ComplexNumber(9,8)
c1.add(c2)
print(c1)
