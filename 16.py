print("**************Result**********************")
name=input("Enter student name:::")
print("Enter the marks of the subject")
sub1=float(input("Subject 1 marks:"))
sub2=float(input("Subject 2 marks:"))
sub3=float(input("Subject 3 marks:"))
sub4=float(input("Subject 4 marks:"))
sub5=float(input("Subject 5 marks:"))
total=(sub1+sub2+sub3+sub4+sub5)
print("Total marks of all the subject is::",+total)
percentage=(total/5)
print("Percentage of the student is ::",+percentage)
if(percentage>=75):
    print("Distinction")
elif(percentage>60 and percentage<=75):
    print("FIrst class")
elif(percentage>=33 and percentage<=60):
    print("Second class")
else:
    print("Fail")
    