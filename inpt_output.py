#input('prompt')
#Example 1 of input

# name=input("Enter your name: ")
# print("My name is, " + name + " and i am beautiful")
 
#Example 2
# number=int(input("Enter the number"))
# product=number*20
# print(product) 

# #Multiple input
# s,r,w=map(int,input("Enter the values").split(" "))
# print("The values are:",end=" ")
# print(s,r,w)

#how to capture input from a tuple
# 1

mylist=list(map(int,input("Enter the  list values : ").split()))
myset=set(map(int,input("Enter the  set values : ").split()))
print(myset)
print(type(myset))
print(mylist)
print(type(mylist))
