#importing randint function for computer choice
from random import randint

#defining a function to print menu bar
def menu_bar():
    print("\nenter:\n1 for Stone")
    print("2 for paper")
    print("3 for Scissors")

#program for deciding winner of the game
def winner(user_choice,comp_choice):
    if user_choice==comp_choice:
        return 0
    if user_choice==1:
        if comp_choice==2:
            return 1
        return 2
    if user_choice==2:
        if comp_choice==3:
            return 1
        return 2
    if user_choice==3:
        if comp_choice==1:
            return 1
        return 2
    
    


#printing rule and some points so that user can understand about game
print("Welcome To Game Stone Paper Scissors\n")
rule=input("do you want to know the rules of the game? say (y/n): ")
if rule=="y":
    print("okay the rules are: ")
    print("1. Stone beats Scissors")
    print("2. Scissors beats Paper")
    print("3. Paper beats Stone")
    print("4. if anyone win a round awarded with 1 point")
    print("5. Play continues until one player reaches a predetermined score")
    print("\nits okay lets play\n\n")
else:
    print("\nits okay lets play\n\n")
    
#insitialize user and computer points to zero
user=0
computer=0
name=input("enter your name: ")
print("\nHello",name,"Your Welcome")

#initializing list of options
options=["","Stone","Scissor","Paper"]

#taking input for winning point
pred_point=int(input("enter winning point: ")) 

#intialize a variable for round count and storing the details of each round
round=0
details=[]

#while loop for playing again and angain round till winner declared
while(user<pred_point and computer<pred_point):

    #printing choice
    menu_bar()
    choice=input("Your Input: ")

    #try block if user enter anything wrong
    try:
        user_choice=int(choice)

    #if user enter other than numbers
    except:
        print("Invalid Choice! Try Again!!!")
        continue
    else:
        #if user input integer other than 1,2 or 3
        if (user_choice>3 or user_choice<1):
            print("Invalid Choice! Try Again!!!")
            continue
        

        #if everything is okay then play start
        print("\nYour Chooses:",options[user_choice])
        comp_choice=randint(1,3)
        print("Computer Chooses:",options[comp_choice])

        #calculating winner and increasing point
        win = winner(user_choice,comp_choice)
        if win==0:
            print("\nIt's Tied")
            details.append("Tied")
        elif win==1:
            print("\nYeah! You Win.. Congratulations")
            details.append("Win")
            user+=1
        else:
            print("\nOh No! You lose.. Better Luck Next Time")
            computer+=1
            details.append("Lose")

        round+=1
        print("\nPoints After Round",round)
        print(name,":",user)
        print("Computer :",computer)

        print("\nLets Play Next Round\n")

#finding which one is win the match
if user==pred_point:
    print("Congratulation! You Won The match by ",user,"-",computer,sep='')
else:
    print("Ohh No! You Lose The match by ",computer,"-",user,sep='')

#if user want details of every rouond
temp=input("Do You Want to know the details of each round You played? say(y/n): ")
if temp=="y":
    print("Here is details: ")
    print(details)
print("\nThanks for Playing\n")
