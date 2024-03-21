print("************SIMPLE CALCULATION TABLE****************")
print('''
    For ADDITION PRESS *1*
    For SUBTRACTION PRESS *2*
    For MULTIPLICATION PRESS *3*
    FOR DIVISION PRESS *4*
      ''')
no=int(input("Enter the number from 1 to 4 to do mathematical operations:::"))
if(no>=1 and no<=4):
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
if(no==1):
    print("ADDITION OF THE TWO NUMBER ARE::",num1+num2)
elif(no==2):
    print("SUBTRACTION OF THE TWO NUMBER ARE::",num1-num2)
elif(no==3):
    print("MULTIPLICATION OF THE TWO NUMBER ARE::",num1*num2)
elif(no==4):
    print("DIVISION OF THE TWO NUMBER ARE::",num1/num2)
else:
    print("Enter the valid number.")