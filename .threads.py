#Thread
#Single Level thread
import threading as t
'''
def author(n):
    print("Author Name : ",n)

#author("Nivetha")

t1=t.Thread(target=author,args=("Mukelswar",))
t1.start()
'''


#Multi level thread
'''
def author(n):
    print("Author Name : ",n)

def book(n):
    print("Book Name : ",n)

def price(n):
    print("Book Price : ",n)

"""
for i in range(5):
    author("Praveen")
    book("Learn Python")
    price(2000)
"""

t1=t.Thread(target=author,args=("Mukelswar",))
t2=t.Thread(target=book,args=("Learn Django",))
t3=t.Thread(target=price,args=(2500,))

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
'''

#Daemon Thread

def author(n):
    print("Author Name : ",n)

t1=t.Thread(target=author,args=("Saravanan",))
t1.setDaemon(True)
print(t1.isDaemon())
t1.start()

















    
