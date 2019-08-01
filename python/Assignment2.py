#Assignment2
n=int(input("Enter Number : "))
dl=[int(i) for i in str(n)]
sum=0
for i in dl:
    sum+=i*i*i
if sum==n:
    print("Given number is Armstrong")
else:
    print("Given number is not Armstrong")
