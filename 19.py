print("************CALCULTION OF THE AREA OF TRIANGLE,RECTANGLE,CIRCLE****************")
print('''
    For Area of Circle PRESS *1*
    For Area of triangle PRESS *2*
    For Area of Reactangle PRESS *3*
      ''')
no=int(input("Enter the number from 1 to 3 to find the areas:::"))
if(no==1):
    r=float(input("Enter the radius of the circle::"))
    print("ARea of the circle is::",3.14*r*r)
elif(no==2):
    h=float(input("ENter the height of the triangle::"))
    b=float(input("Enter the base of the triangle::"))
    print("SUBTRACTION OF THE TWO NUMBER ARE::",(b*h)/2)
elif(no==3):
    l=float(input("Enter the length of rectangle:::"))
    b=float(input("Enter the breadth of rectangle::"))
    print("MULTIPLICATION OF THE TWO NUMBER ARE::",l*b)
else:
    print("Enter the valid number.")
