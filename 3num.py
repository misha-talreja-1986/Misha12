# print("Program for making the square and cube of the number")
# num=int(input("Enter the number:"))
# print("Sqaure of the number is:")
# print(num*num)
# print("Cube of the number is:")
# print(num*num*num)
even=0
odd=0
num=int(input("Enter the number:"))
for i in range(0,num):  
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)