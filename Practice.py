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
      





#oops

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

#     def get_info(self):
#         print(f"price of {self.name}is Rs {self.price}")  

# p1=product("phone",10_000)
# p2=product("laptop",40_000)

# p1.get_info()




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





class BankAccount:
    bank_name="SBI"
    def __init__(self,Account_holder,balance):
        self.Account_holder=Account_holder
        self.balance=balance

Account_1=BankAccount("Ali",10_000)
Account_2=BankAccount("Rahul",20_000)

BankAccount.bank_name="HDFC"
Account_1.bank_name="ICICI"

print(Account_1.Account_holder,Account_1.balance,Account_1.bank_name)

print(Account_2.Account_holder,Account_2.balance,Account_2.bank_name)