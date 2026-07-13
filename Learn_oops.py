#Oops --> Class
"""
class class_name:
    set of Attributes and functions
    def fun_name(self,):
        #block of code

varible = class_name()
"""
class Mobile:
    Brand = None
    Model = None
    Color = None
    price = None
    def button(self):
        print(self.Model,"It's Helps to Display ON/OFF..")

# m1 = Mobile()
# print(m1.Brand)
# m1.Brand = "Samsung"
# m1.Model = "Samsung S25"
# m1.Color = "Black"
# m1.price = 50000
# print("Brand : ",m1.Brand)
# print("Model : ",m1.Model)
# print("Color : ",m1.Color)
# print("Price : ",m1.price)
# m1.button()
# print("""********************""")
# m2 = Mobile()
# print(m2.Brand)
# m2.Brand = "Samsung"
# m2.Model = "Samsung S26 Ultra"
# m2.Color = "White"
# m2.price = 125000
# print("Brand : ",m2.Brand)
# print("Model : ",m2.Model)
# print("Color : ",m2.Color)
# print("Price : ",m2.price)
# m2.button()


#Inhertance
#Single level Inheritance...
class Ebook:
    book = "Learn Python"
    def fun1(self):
        print("Book Name : ",self.book)

class Book_author(Ebook):
    author = "Mukleshwar"
    def fun2(self):
        print("Author Name : ",self.author)

# a = Book_author()
# print(a.book)
# print(a.author)
# a.fun1()
# a.fun2()

# Multi-level inheritance

class Ebook:
    book = "Learn Python"
    def fun1(self):
        print("Book Name : ",self.book)

class Author(Ebook):
    author = "Mukleshwar"
    def fun2(self):
        print("Author Name : ",self.author)

class Book_genre(Author):
    def fun3(self):
        print("Book genre : Progamming Skills")

# g = Book_genre()
# g.fun3()
# g.fun2()
# g.fun1()
# print(g.book)
# print(g.author)


#Hierachical Inheritance
class UPI:
    def fun1(self):
        print("UPI Money Trafer System")

class Gpay(UPI):
    def fun2(self):
        print("Gpay Money Trafer System from UPI")

class Phonpe(UPI):
    def fun3(self):
        print("Phone Money Trafer System from UPI")

# G = Gpay()
# Ph = Phonpe()
# G.fun1()
# G.fun2()
# Ph.fun3()
# Ph.fun1()


class Music_palyer:
    def fun1(self):
        print("Play the Music")

class Camera:
    def fun2(self):
        print("Camera to Take Good Pictures")

class Phone(Music_palyer,Camera):
    def fun3(self):
        print("Connect Your Network with call")

p = Phone()
p.fun3()
p.fun1()
p.fun2()