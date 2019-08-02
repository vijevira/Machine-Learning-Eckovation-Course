def print_menu():
    
    print("Enter:\n1 for addition\n2 for substraction\n 3 for multiplication\n4 for devision")
def myfunc():
    
    choice=True
    while(choice):
        input1=float(input("enter first number: "))
        input2=float(input("enter second number: "))
        print_menu()
        ch=int(input())
        if ch==1:
            print("The answer=",input1+input2)
        elif ch==2:
            print("The answer=",input1-input2)
        elif ch==3:
            print("The answer=",input1*input2)
        elif ch==4:
            try:
                print("The answer=",input1/input2)
            except:
                print("devision by zero not possible")
        else:
            print("please enter a valid chioice")
            
        c=input("Do you want to continue? (y/n)")
        if c=="n":
            choice=False
            
        
myfunc()

