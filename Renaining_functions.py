#Return type function
#return -> keyword
"""
1.return type without argument function
2.return type with argument function

Syntax of return type:
def function_name(arguments):
    #block of code
    #return value

variable = function()
"""

# 1.return type without argument function
def add():
    a = 10
    b = 20
    c = a + b
    return c

#print(add())
# v = add()
# print("Add : ",v)


# 2.return type with argument function
def sub(x,y):
    a = x
    b = y
    c = a - b
    return c

#print(add())
# v = sub(500,200)
# print("Subtract value : ",v)


#armstrong
def armstrong(number):
    l = len(str(number))
    a = number
    b = 0
    t = a
    while t>0:
        d = t % 10
        b+=d**l
        t //= 10
    if b == a:
        return f"{b} is an armstrong number."
    else:
        return f"{b} is not an armstrong number."

# n = int(input("Enter a number: "))
# v = armstrong(n)
# print(v)

#lambda or single line function
"""
variable = lambda arg : expression
"""
# a = lambda a,b,c : a+b+c
# print(a(10,20,30))

#recursive function
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
v = fact(6)
print("factorial :",v)
"""
return 5*fact(4) -> 5*
return 4*fact(3) -> 5*4* = 20*
return 3*fact(2) -> 20*3* = 60*
return 2*fact(1) -> 60*2* = 120*
return 1 => 120*1 = 120
"""

#user register & login
def login():
    print("login function")
    username = input("Enter your username: ")
    if username == name:
        pas = input("Enter your password: ")
        if pas == password:
            print("Login Successful")
        else:
            print("Wrong Password")
            login()
    else:
        print("Invalid username")
        login()

def register():
    global name, password
    print("register function")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    login()
register()












