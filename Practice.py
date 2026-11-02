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


def fun(n):
    while n>0:
        print(n%10)
        n=n//10

print(fun(4321))
      
