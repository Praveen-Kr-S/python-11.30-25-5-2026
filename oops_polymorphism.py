#Oops_polymorphism
#Single class with multiple fuctions with same name
#but pass the difrrent arguments

class calcutor:
    def add(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print("4 arguments add va,b,c,dalue : ", a + b + c + d)
        elif a!=None and b!=None and c!=None:
            print("3 arguments add value : ", a + b + c)
        elif a!=None and b!=None:
            print("2 arguments add value : ",a+b)
        else:
            print("1 arguments value : ",a)

    # def add(self,a,b,c,d):
    #     print("4 arguments add va,b,c,dalue : ",a+b+c+d)
    #
    # def add(self,a,b,c):
    #     print("3 arguments add value : ",a+b+c)
    #
    # def add(self,a,b):
    #     print("2 arguments add value : ",a+b)
    #
    # def add(self,a):
    #     print("1 arguments value : ",a)

# c = calcutor()
# c.add(45)
# c.add(45,60,45,67)
# c.add(20,40,10)
# c.add(20,40)

# Method overriding
# class book:
#     def fun1(self):
#         print("Book Name : Learn Java")
# class author(book):
#     def fun1(self):
#         super().fun1()
#         print("Author Name : Vinoth")
# class price(author):
#     def fun1(self):
#         super().fun1()
#         print("Book Price : 500")
#
# p = price()
# p.fun1()

#Operator Overloading

# a = 45
# b = " Kumar"
# c = 10
# # print(a+b)
# print(a.__add__(b))
# print(a.__add__(c))
#
# print(a.__sub__(c))
# print(a.__sub__(b))


# Abstraction in Python
"""
abc -> module
ABC -> bulid in class
abstractmethod -> function
"""
from abc import ABC,abstractmethod
class Zoho(ABC):
    @abstractmethod
    def zoho_pay(self):
        print("Product Name : zoho pay")
        print("Brand Name : zoho")
        print("Brand Address : zoho")
        print("Product Sensitive content")

    @abstractmethod
    def zoho_school(self):
        print("Product Name : zoho school")
        print("Brand Name : zoho")

class users(Zoho):
    def zoho_pay(self):
        # super().zoho_pay()
        print("Product Name : zoho pay")
        print("Brand Name : zoho")

    def zoho_school(self):
        print("Product Name : zoho school")


# u = users()
# u.zoho_pay()

#Encapsulation
"""
__variable => private
_variable => protected
variable => public
"""
class Upi:
    name = "Praveen Kumar"
    _ac = 12566654324
    __pin = None
    def __get_pin(self,p):
        self.__pin = p
        # return self.__pin
    def show(self,p):
        self.__get_pin(p)

class user(Upi):
    def demo(self):
        print(super().name)
        # print(super().__pin)

# u = Upi()
# print(u.name)
# # print(u.__pin)
# # print(u._ac)

# u.show(8765)
# user().demo()


# Constructor
"""
class class_name:
    def __init__(self):
        #block of code
"""
class Mobile:
    brand = None
    model = None
    color = None
    price = None

    def __init__(self,**s):
        # print(s)
        self.brand = s.get("b")
        self.model = s.get("m")
        self.color = s.get("c")
        self.price = s["p"]
        print("Mobile Brand : ",self.brand)
        print("Mobile Model : ",self.model)
        print("Mobile color : ",self.color)
        print("Mobile Price : ",self.price)
        print("=========================")

# m1 = Mobile("Samsung","S26","black",85000)
# m2 = Mobile("Realme","P3 Ultra","red",35000)
# m3 = Mobile(b = "Apple",m = "Iphone 17",c = "Black",p = 120000)
