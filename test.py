# class test:
#     def get_name(self):
#         self.name=input("Enter your name :")
#     def get_age(self):
#         self.age=int(input("Enter your age"))
#     def disp_name(self):
#         print('name',self.name)
#     def disp_age(self):
#         print('age',self.age)
# obj=test()
# obj.get_name()
# obj.get_age()
# obj.disp_name()
# obj.disp_age()

# l=int(input("Enter the limit"))
# for i in range(1,l+1):
#     for j in range(l+1,i,-1):
#         print(end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print("\n")

# def factorial(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input("Enter number"))
# print("factorial of",n,"is",factorial(n))

# import numpy as np
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# b=np.zeros((5,5))
# print(b)
# print(a)

# a=np.array([1,2,3,8])
# b=np.array([4,5,6,8])
# c=np.sum((a,b),axis=1)
# print(c)
import pandas as pd
# data=[1,"two",5.0,"ten"]
# k=pd.Series(data)
# print(k)
# print(type(k))

# s={'Vehicle':['bmw','audi','benz','pulser'],'Type':['car','car','car','bike']}
# for i in s.items():
#     print(i)
# k=pd.DataFrame(s).groupby('Type').count()
# print(k)

# df=pd.DataFrame()
# car=['bwm','audi','benz']
# bike=['pulser','bajaj','hero']
# df['cars']=car
# df['bikes']=bike
# print(df)


# cars=['bwm','audi','benz']
# bike=['pulser','bajaj','hero']
# c={"cars":cars,"bikes":bike}
# print(pd.DataFrame(c))

# l1=[1,2,3,"red","apple"]
# l2=[5,6,7,8,9]
# z=zip(l1,l2)
# k=(list(z))

# for l1,l2 in enumerate(zip(l1,l2)):
#     print(l1,l2)
# ul1,ul2=zip(*k)
# print(ul1)
# print(ul2)

# def fun(n):
#     x=lambda a:a+n
#     print(x(8))
# fun(10)

# def kwarg(**kw):
#     print(kw['mob'])
# kwarg(name='hi',mob=234)

# def arg(*a):
#     for i in a:
#         print(i)
#         print(type(a))
# arg(1,2,3,4,5,6,7,7,8,)

x=int(input("enter a number"))
sum=0
while x!=0:
    rem=x%10
    rem=rem+1
    sum=rem+sum*10
    x=x//10
print(sum)