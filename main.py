# print
# print("Hello kya haal chaal")


#    2 variable
# a=1  # rule 1)not start with number 2)not use space 3)not used special char exept _
# print(a)

# HozaifaShaikh=3 #pascal case
# hozaifaShaikh=4 #camel case
# hozaifa_shaikh=6 #snake case

  #  3 Data Type

# a=4        #integer
# b=22/7  #float
# c=34+5j # complex
# d="My name is Hozaifa"   #string
# e=True #bollean
# print(type(a),type(b),type(c),type(d),type(e))


# 4  String & type conversion

# a="HOZAIFA"
# print(a[3])
# print(a[0:6:1])  #[start:stop:Step]
 
 #type conversion
# a=7
# a=str(a)
# print(type(a))

# 05 input  and output 

# name ="Hozaifa"
# age="23"
# print("my name is",name,"and age is ",age)  # normal string print
# print(f"my name is {name} and my age is{age}")   #f string print f

# age=int((input("Enter your Age")))

# # print("Your age is ",age)
# print(type(age))

# ex
# num=int(input("Enter the number "))
# age=int(input("Enter your age "))
# print(f"Your number is  {num} your age is {age}")

#Operator

# a=20
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

# Assignment operator

# a=23
# compund assignment operator

# a=20
# # a=a+20   
# a+=20
# print(a)

#comparison operator
  
# a=12.1
# b=12

# print(a==b)
# print(a>b)
# print(a!=b)

#  string  compare with  string
# print(ord("a"))
# print(ord("b"))

# print("a">"b")

# logical operator

# print((12==12) and (13>17))

# print( not 12==12)
# print(12==12 or 15<12)

# print(126 >130)
# print((456==456) != (235==236))
# print(12<10 or 45==45 or 69>70)
# print(True and (bool(0)))


# conditional Statement
#  if 

# a=10
# if a>5:
#     print("Do Work")

#if else

# a=int(input("Enter a Number  "))
# if a>20:
#     print("TAsk A")
# else:
#     print("Task B")


#if elif else

# a=int(int(input("Enter the Number  "  )))
# if a<10:
#     print(" TAsk A")
# elif a<20:
#     print("Task B")
# else:
#     print("Task C")


# Q1  accepet two and print greater 

# num1=int(input("Enter num 1 " ))
# num2=int(input("Enter num 2 "))
# if num1>num2:
#     print("num1 is Greater")
# else:
#     print("num2 is Greater")

# Q2

# gen=input("Enter the gender")
# if gen=="M":
#     print("Good morning Sir")
# else:
#     print("Good morning mam")


# Q3

# num=int(input("Enter the number"  ))
# if num%2==0:
#     print("number is even")
# else :
#     print("number is odd")

# # Q4

# name=input("Enter the Name : ")
# age=int(input("Enter the age : "))
# age1=18-age
# if age>=18:
#     print(f"Hello {name} you are Valid for Vote")
# else:
#     print(f"Hello{name} You are not valid for vote try after {age1}")

#Q5 Leap Year

# year=int(input("Enter thr year : "))
# if year%100==0 and  year%400==0:
#     print("Leap year")
# elif year%100!=0 and year%4==0:
#     print("Leap year")
# else:
#     print("Not Leap year")


# tem=int(input("Enter the temp "))
# if tem<0:
#     print("Freezing cold")
# elif tem<=10 :
#     print("Very Cold")
# elif tem<20:
#     print("cold")
# elif tem<30:
#     print("Pleasent")
# elif tem<40:
#     print("Hot")
# else:
#     print("Very Hot")




#For Loop

# a=range(1,21,1)
# for i in a:
#     print(i)
 
# directly range
# for i in range(1,21,2):
#     print(i)
    

# table of 5

# for i in range(5,51,5):
#     print(i)

# num=int(input("Enter the number " ))
# for i in range(num,num*10+1,num):
#     print(i)

# loop for string
# a="Hozaifa"
# for i in range(5):
#     print(a[i])

# a="HOZAIFA" 
# print(len(a))
# for i in range(len(a)):
#     print(a[i])

# a="Hozaifa"
# for i in a:
#     print(i)

# #break and continue statement

# for i in range(1,21,1):
#     if i==15:
#         continue
#     print(i)




#print hello world n njumber times
# n=int(input("Enter the Number"))
# for i in range(n):
#     print("Hello world")

# n=int(input("Enter the Number"))
# for i in range(1,n+1,1):
#     print(i)


# n=int(input("enter the number"))
# for i in range(n,0,-1):
#     print(i)

#Table
# n=int(input("Enter the number  "))
# for i in range(1,11,1):
#     print(f"{n}*{i}={n*i}")

# n=int(input("Enter the  number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(f"The sum is {sum}")


# n=int(input("Enter the number"))
# mul=1
# for i in range(1,n+1):
#     mul=mul*i

# print(f"the number is {mul}")    






#odd even sum

# n=int(input("Enter the  number  "))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even=even+i
#     else:
#         odd=odd+i
# print(f"the even and odd sum is ,{odd},{even}")       




#facator


# n=int(input("enter the number you want factor :-"))
# for i in range(1,n+1):
#     if   n%i==0:
#         print(i)




# #Check perfect number or not
# n=int(input("enter the number"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i

# if sum==n:
#     print("the numnber is perfecrt")

# else:
#     print("the nunber is not perfect")


# #check numner is  prime or not

# n=int(input("Enter the number :"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count=count+1
        
# if count==2:
#     print("Prime  number")
# else:
#     print("Not Prime")

# #reverse the string

# a="HOZAIFA"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]

# print(b)


# # palindrome
 
# a="naman"
# b="" 
# for i in range(len(a)-1,-1,-1):
#       b=b+a[i]
# if a==b:
#       print("Palindrome")
# else:
#       print("Not palindrome")



#count character number etc

# a="xjebdhb23253354@##$%"
# char=0
# num=0
# spch=0
# for i in a:
#     if i.isdigit():
#         num+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spch+=1


# print(f"The Character is {char}\nand the number is {num}\n the special charcacter is {spch}")            
      

# import random

# num=random.randint(1,10)
# tries=0
# while True:
#     guess=int(input("please guess your number between 1 to 10 :-"))
#     if num==guess:
#         tries+=1
#         print(f"you are right you guessed the numberis {tries} tries")
#         break
#     elif num<guess:
#         print("go a little lower")
#         tries+=1
#     elif num>guess:
#         print("go a little higher")
#         tries+=1  
#     else:
#         tries +=1
#         print("sorry you are wrong")    


#FUNCTION

# def hello():
#     print("Hello how are you function")

# hello()



# #plaindrom in function

# def palindrom(str):
#     rev=""
#     for i in range(len(str)-1,-1,-1):
#         rev=rev+str[i]
#     if rev==str:
#         print(f"{str} is a palindrom")
#     else:
#         print("Not a palindrom")    

# palindrom("cat")
# palindrom("cac")           



# Data Structure    List, Tuple, Set, Dictionry

# a=[12,13,12,13]
# print(a[1:3])
 

# a=[1,2,3,4,5]
# # a.append(6)
# a.insert(2,3)
# print(a)


# a=[23,-32,98,-2,23,-25]
# positive=[]

# for i in a:
#     if i>=0:
#         positive.append(i)
# print(f"The Positive number is{positive}")        

#Mean 
# a=[12,13,12,1,23,22]
# sum=0
# for i in a:
#     sum=sum+i

# mean=sum/len(a)  
# print(mean)
    

#greatest number
# a=[212,22,33,232,22,76,766]
# largest=a[0]
# index=0
# for i in range(len(a)):
#     if a[i]>largest:
#         largest=a[i]
#         index=i
# print(f"your largest number is {largest} at index{index}")     





# # second largest and largest number
# l=[1,12,23,3,2,43,32]
# largest=l[0]
# sec_largest=l[0]

# for i in l:
#     if i>largest:
#         sec_largest=largest
#         largest=i
#     elif i>sec_largest:
#         sec_largest=i

# print(sec_largest,largest)   



#check list is sorted or not

# l=[12,13,14,1,5]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")  





#Tuple

# a=(1,2,3,4,5,6)

# # for i in a:
# #     print(a[i])

# count=a.count(5)
# print(count)



#set
# s={1,2,3,45,4}
# print(type(a))


# a={1,3,4,5}
# a.add(2)
# a.remove(4)
# print(a)


# a={1,2,3,4,5}
# b={3,4,5,6,7}
# # s=a.union(b)
# # s=a.intersection(b)
# # s=a.difference(b)
# s=a.symmetric_difference(b)
# print(s)





#DICTIONAY

# d={10:100,20:200,30:300}
# # print(d)
# # d[10]=1000
# # print(d)
# d.update({50:500})
# print(d)




#count a frequency of each element in list
# a=[1,1,1,2,3,3,3,3,4,4,5,6]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)            



# d1={10:100,20:200,40:300}
# d2={40:400,50:500,60:600}
# for i in d2:
#     if i in d1.keys():
#         d1[i]+=d2[i]
#     else:
#         d1[i]=d2[i] 



#exceptional Handling

# p=open(r"C:\Users\hozai\Desktop\text.txt")
# print(p.read())

# r=open('Superman.txt','a')
# r.write('append ing the element')












#mutilevel inheritance

class Factory:
    def __init__(self,material,zips):
        self.material=material
        self.zips=zips

class BhopalFactory(Factory):
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color=color

class Punefactory(BhopalFactory):
    def __init__(self,material,zips,color,pockets):
        super().__init__(material,zips,color)
        self.pockets=pockets     

obj=Punefactory()               
    