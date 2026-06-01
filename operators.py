#comparision operator/conditional/relational
#==,!=, >, <, >=, <=
'''
a = 10
b = 20
c = 10
d = 30

print(a == b)#10 == 20
print(a != b)
print(a == c)
print(a > b)
print(d < b)
print(a >= c)
'''
#logical operator
#and, or, not
#and -> check all the condition if true, it's give true
#or -> check the if any on condition is true -> if condition true -> (or) return the true 
#not(Condition) ->  if condition return true -> o/p false
#                   if condition return false -> o/p true
'''
x = 'u'

#print(x >= 2 and x <= 10 and x == 6)
#print(x >= 2 or x <= 10 or x == 6)
print(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x=='u')
print(not(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x=='u'))
'''


#Condional Statement
#if Statement
"""
if condition:
    #True Statement
"""
#1
b = 10
if b == 0:
    print("b is zero..")

#if-else
"""
if condition:
    #True Statement
else:
    #False Statement
"""   
#2 -> take two variables in integer data
#     if m>n is true ->: findthat two value quation and remainder
'''
m = int(input("Enter m value :"))
n = int(input("Enter n value :"))

if m>n:
    print("Quation : ",m//n)
    print("Remainder : ",m%n)
else:
    print("**** m is lessthan n ****")
'''

'''
#3 odd / even
b = 83
if(b%2 == 0):
    print(b,"is even number")
else:
    print(b," is odd number")


#4 positive / negative
b = 0
if(b > 0):
    print(b,"is positive number")
else:
    print(b," is negative number")

'''

#if - elif -else
#5
"""
if condition:
    #True Statement
elif condition:
    #True Statement
elif condition:
    #True Statement
else:
    #False Statement
"""
b = 10
'''
if b == 0:
    print("b is zero..")
elif b > 0:
    print(b,"is positive number")
else:
    print(b," is negative number")
'''
#6
"""
1-5 -> 3
6-10 -> 5
10-15 -> 7
above 15 -> 10
"""
'''
d = int(input("Enter Count Of Day : "))
if(d>=1 and d<=5):
    print("Book charges Rs :",d*3)
elif(d>=6 and d<=10):
    print("Book charges Rs :",d*5)
elif(d>=10 and d<=15):
    print("Book charges Rs :",d*7)
elif(d>=16):
    print("Book charges Rs :",d*10)
else:
    print("Give proper value with positive numbers")
'''


#Nested if
"""
Syntax of nested if

if condition:
    if condition:
        #True Statement
    else:
        #False Statement
else:
    #False Statement
"""
email = input("Enter the Email : ")
if email == "pk@gmail.com":
    pa = int(input("Enter the Password : "))
    if pa == 1234:
        print("Login Success")
    else:
        print("Invalid Password")

else:
    print("Invalid email id")




























    



































