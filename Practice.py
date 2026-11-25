# colour=input("Enter the colour ").lower()
# if colour=="red":
#     print("Stop")
# elif  colour=="yellow":
#     print("Ready")
# elif colour=="green":
#     print("GO")
# else:
#     print("Invalid Colour")         




#Factorial of n by usnig function
# def fac(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i

#     return fact
   
# print(fac(5))



#fundamental part 2

# salary=int(input("Enter the Salary : "))

# if salary<30000:
#     tax=salary*5/100
#     print(f"you have to pay  {tax}")
# elif salary>=30000 or salary<=70000:
#     tax=salary*15/100
#     print(f"you have to pay  {tax}")
# else:
#     tax=salary*25/100
#     print(f"you have to pay  {tax}")

  

# def even_number(a,b):
#     # even=0
#     for i in range(a,b+1):
#         if i%2==0:
#     #      even=even+i
#     # return even    
#          print(i)

# even_number(1,10)         


# def fun(n):
#     while n>0:
#         print(n%10)
#         n=n//10

# print(fun(4321))
      







#OOPS
# class Employee:
#     company="tcs"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# Employee_1=Employee("Ali",25_000)
# Employee_2=Employee("Rahul",30_000)

# # print(Employee_1.name)
# # print(Employee_1.salary)
# # print(Employee.company)

# # print(Employee_2.name)
# # print(Employee_2.salary)
# # print(Employee.company)

# Employee.company="Infosys"
# Employee_1.company="Wipro"
# del Employee_1.company
# print(Employee_1.company)
# print(Employee_2.company)



# class car:
#     wheels=4
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color

# Car_1=car("Toyota","White")    
# Car_2=car("Honda","Black")   

# car.wheels=6
# print(Car_1.brand,Car_1.color,Car_1.wheels)
# print(Car_2.brand,Car_2.color,Car_2.wheels)



#self
# class Mobile:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
        
#     def show_details(self):
#         print(f"{self.brand} {self.price}")

#     def apply_discount(self,discount):
#         self.price=self.price-discount    

# c1=Mobile("Samsung",20_000)
# c2=Mobile("Iphone",70_000)   

# c1.show_details()
# c2.show_details()
# c1.apply_discount(1000)
# c1.show_details()



#class method

# class mobile:
#     company="ABC mobiles"

#     @classmethod
#     def change_company(cls,new_name):
#         cls.company=new_name

# m1=mobile()
# m2=mobile()

# mobile.change_company("DS Mobile")

# print(m1.company)
# print(m2.company)



#oops  product store example

# class product:
#     count=0
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         product.count+=1

#     def get_info(self):
#         print(f"price of {self.name}is Rs {self.price}") 

#     @classmethod
#     def product_count(cls):
#         print(f"the count  is {cls.count}")    

#     @staticmethod
#     def get     

# p1=product("phone",10_000)
# p2=product("laptop",40_000)

# # p1.get_info()
# product.product_count()


# # Inheritance
# class Employee:
#     start_time="10 am"
#     end_time="6 pm"

# class teacher(Employee):
#     def __init__(self,subject):
#         self.subject=subject

#     def change_time(self,new_end_time):#for change time
#         self.end_time=new_end_time
   
# class admin(Employee):
#     def  __init__(self,manager):
#         self.manager=manager

# admin_1=admin("rahul")

      
# t1=teacher("Maths")
# # t1.change_time("5 pm")

# # print(t1.subject,t1.start_time,t1.end_time)


# print(admin_1.manager,admin_1.start_time,admin_1.end_time)
# print(t1.end_time)


#abstarction
# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")

# class Cow(Animal):
#     def make_sound(self):
#         print("meow")

# lion=Lion()
# lion.make_sound()




#Polymorphism


#funation overriding
# class Employee:
#     def get_designation(self):
#         print("designation=Employer")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation=teacher")  

# t1=Teacher()  
# t1.get_designation()


#file handling


#read file
# f=open("Superman.txt","r")
# print(f.read(5))

#write file
# f=open("Superman.txt","a")
# f.write("\n superman is super Hero")

#with keyword
# with open("Superman.txt","r") as f:
#     print(f.read())

#delete file
# import os
# os.remove("check.txt")



# #Exception handling

# try:
#     x=int(input("Enter the numner : "))
#     Ans=10/x
# except ZeroDivisionError:
#     print("Canot dide by zero")
# except ValueError:
#     print("Enter the valid value")
# else:
#  print(f"thye answer is{Ans}  ")
# finally:
#    print("the final program end")

#list Comprehension

#using for loop
# sq=[]
# for i in range(6):
#     sq.append(i*i)

# print(sq)    

# # using list complrehension
# square=[i*i for i in range(6) if i%2==0]
# print(square)


# num=[-1,-3,6,-5,0,5,6]
# num=[0 if val < 0 else val for val in num ]
# print(num)
