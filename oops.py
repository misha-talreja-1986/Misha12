# class Car:
#     def __init__(self,cname,model,price):
#         self.cname=cname
#         self.model=model
#         self.price=price

# audi=Car("Audi",'q10',8000000)
# print(audi.cname)
        


# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age

# P1=Person("Chirag","Joshi",90)
# print(P1.fname)




# instance method 

# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def full_name(self):
#         return f"Your full Details full name {self.fname} {self.lname} {self.age}"
#     def is_above_18(self):

#         if self.age>=18:
#             return True
#         else:
#             return False
# P1=Person("Chirag","Joshi",9)

# print(P1.__dict__)
# print(P1.full_name())
# print(P1.is_above_18())

# class Circle:
#     def __init__(self,pi,radius):
#         self.pi=pi
#         self.radius=radius
#     def cal_circumference(self):
#         return 2*self.pi*self.radius
# C=Circle(3.14,5)
# C1=Circle(3.14,4)
# print(C.cal_circumference())
# print(C1.cal_circumference())

# memorywaste
# class variable 

# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def cal_circumference(self):
#         return 2*Circle.pi*self.radius
# C=Circle(5)
# C1=Circle(4)
# print(C.cal_circumference())
# print(C1.cal_circumference())










# class Car:
#     @classmethod
#     def test(cls):
#         print("test")

# Car.test()





# class Person:
#     count_in=0
#     def __init__(self,fname,lname,age):
#         Person.count_in+=1
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     @classmethod
#     def count_method(cls):
#         return cls.count_in
        

# P1=Person("Chirag","Joshi",90)
# P2=Person("Chirag","Joshi",90)
# P3=Person("Chirag","Joshi",90)

# print(Person.count_method())


# Class method as constctor 

# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#     def full_name(self):
#         return f"Your full details is {self.first_name} {self.last_name} {self.age}"
#     @classmethod
#     def from_string(cls,string):
#         first,last,age=string.split()
#         return cls(first,last,age)

# P2=Person("chirag","Joshi",90)
# P1=Person.from_string("Chirag joshi 89")

# print(P1.full_name())
# print(P2.full_name())


# class Person:
#     @staticmethod 
#     def hello():
#         return "I am static method..."
    
# print(Person.hello())


# Abstraction

# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#     def full_name(self):
#         return f"Your full details is {self.first_name} {self.last_name} {self.age}"
# P1=Person("Chirag","Joshi",52)
# P1.first_name="DDDD"
# print(P1.full_name())


# inheritance


# class A:
#     @staticmethod
#     def a():
#         print("A")

# class B(A):
#     pass

# B.a()
# class Phone:
#     def __init__(self,brnad_name,model_name,price):
#         self.brand_name=brnad_name
#         self.model_name=model_name
#         self.price=price

# class SmartPhone(Phone):
#     def __init__(self, brnad_name, model_name, price,cam):
#         super().__init__(brnad_name, model_name, price)
#         self.cam=cam

# 2nd method of inheritance
# class Phone:
#     def __init__(self,brnad_name,model_name,price):
#         self.brand_name=brnad_name
#         self.model_name=model_name
#         self.price=price

# class SmartPhone(Phone):
#     def __init__(self, brnad_name, model_name, price,cam):
#         #super().__init__(brnad_name, model_name, price)
#         Phone.__init__(self,brnad_name,model_name,price)
#         self.cam=cam

# # P1=Phone("Nokia",'3310',3000)
# S1=SmartPhone("Nokia",'3310',3000,'12mp')
# print(S1.brand_name)

# class A:
#     @staticmethod
#     def a():
#         print("100")
# class B(A):
#     @staticmethod
#     def b():
#         print("200")
# class C(B):
#     def c():
#         print("300")

# C.a()
# C.b()
# C.c()



# class Phone:
#     def __init__(self,brnad_name,model_name,price):
#         self.brand_name=brnad_name
#         self.model_name=model_name
#         self.price=price

# class SmartPhone(Phone):
#     def __init__(self, brnad_name, model_name, price,cam):
#         super().__init__(brnad_name, model_name, price)
#         self.cam=cam

# class Flagship(SmartPhone):
#     def __init__(self, brnad_name, model_name, price, cam,ram):
#         super().__init__(brnad_name, model_name, price, cam)
#         self.ram=ram
# F1=Flagship("Nokia",'3310',3000,'12mp','2gb')
# print(F1.price)


# class A:
#     @staticmethod
#     def a():
#         print("100")
# class B:
#     @staticmethod
#     def b():
#         print("200")
# class C(A,B):
#     def c():
#         print("300")

# C.a()
# C.b()
# C.c()


# method resolution 
# class Phone:
#     def __init__(self,brnad_name,model_name,price):
#         self.brand_name=brnad_name
#         self.model_name=model_name
#         self.price=price
#     def full_details(self):
#         return f"your Phone Details {self.brand_name} {self.model_name} {self.price}"

# class SmartPhone(Phone):
#     def __init__(self, brnad_name, model_name, price,cam):
#         super().__init__(brnad_name, model_name, price)
#         self.cam=cam

# class Flagship(SmartPhone):
#     def __init__(self, brnad_name, model_name, price, cam,ram):
#         super().__init__(brnad_name, model_name, price, cam)
#         self.ram=ram
# F1=Flagship("Nokia",'3310',3000,'12mp','2gb')
# print(help(Flagship))

# method overriding 
# class Phone:
#     def __init__(self,brnad_name,model_name,price):
#         self.brand_name=brnad_name
#         self.model_name=model_name
#         self.price=price
#     def full_details(self):
#         return f"your Phone Details {self.brand_name} {self.model_name} {self.price}"

# class SmartPhone(Phone):
#     def __init__(self, brnad_name, model_name, price,cam):
#         super().__init__(brnad_name, model_name, price)
#         self.cam=cam
#     def full_details(self):
#         return f"your Phone Details {self.brand_name} {self.model_name} {self.price} {self.cam}"

# class Flagship(SmartPhone):
#     def __init__(self, brnad_name, model_name, price, cam,ram):
#         super().__init__(brnad_name, model_name, price, cam)
#         self.ram=ram

# F1=Flagship("Nokia",'3310',3000,'12mp','2gb')

# print(F1.full_details())





# class Phone:
#     def __init__(self,brnad_name,model_name,price):
#         self.brand_name=brnad_name
#         self.model_name=model_name
#         self.price=price
#     def full_details(self):
#         return f"your Phone Details {self.brand_name} {self.model_name} {self.price}"

# class SmartPhone(Phone):
#     def __init__(self, brnad_name, model_name, price,cam):
#         super().__init__(brnad_name, model_name, price)
#         self.cam=cam
#     def full_details(self):
#         return f"your Phone Details {self.brand_name} {self.model_name} {self.price} {self.cam}"

# class Flagship(SmartPhone):
#     def __init__(self, brnad_name, model_name, price, cam,ram):
#         super().__init__(brnad_name, model_name, price, cam)
#         self.ram=ram
        
# F1=Flagship("Nokia",'3310',3000,'12mp','2gb')
# S1=SmartPhone("Nokia",'3310',3000,'12mp')


# print(isinstance(F1,Phone))
# print(isinstance(S1,Flagship))

# print(issubclass(Flagship,SmartPhone))
# print(issubclass(Phone,SmartPhone))


# megic method and dunder method 

# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
    # def __str__(self):
    #     return f"{self.fname} {self.lname} {self.age}"
    # def __repr__(self):
    #     return f"{self.fname} {self.lname} {self.age}"

# P1=Person("Chirag","Joshi",90)
# print(P1)

# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     # def __str__(self):
#     #     return f"{self.fname} {self.lname} {self.age}"
#     # def __repr__(self):
#     #     return f"{self.fname} {self.lname} {self.age}"
    # def __add__(self,other):
    #     return self.age+other.age

# P1=Person("Chirag","Joshi",90)
# P2=Person("Chirag","Joshi",90)

# print(P1+P2)


# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def name_change(self):
#         name=input("Enter your new name::")
#         self.fname=name
#         return f"Your name change and your full name is {self.fname} {self.lname}"

# P1=Person("Chirag","Joshi",90)
# print(P1.name_change())