#FIND the max number from the given three number
num1=int(input("Enter the first  number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if(num1==num2 and num1==num3):
    print("All the values are same")
elif(num1==num2):
    if(num3>num1 and num3>num2):
        print("number 3 is maximum")
    else:
        print("Num1 amd num2 are same so they are are maximum")
elif(num1==num3):
    if(num2>num1 and num2>num3):
        print("Number 2 is maximum")
    else:
        print("Number 1 and 3 are same so they are maximum")
elif(num2==num3):
    if(num1>num2 and num1>num3):
        print("Number 1 is maximum")
    else:
        print("Number 2 and 3  are same so they are maximum")
else:
    if(num1>num2 and num1>num3):
        print("NUm1 is maximum")
    elif(num2>num1 and num2>num3):
        print("Number 2 is maximum")
    else:
        print("Number 3 is maximum")