#String
#-->1.String Indexing

"""
String is sequence of characters

Bk Index :    -6 -5 -4 -3 -2 -1 
         a =  "P  Y  T  H  O  N"
Fw Index :     0  1  2  3  4  5
Length   :     1  2  3  4  5  6
"""
'''
a = "PYTHON"
print(a)
print(a[2])
print(a[-4])
print(a[5])
print(a[-6])

#-->2.String Slicing
#variable[start:stop(n-1)]
s = "I am Praveen Kumar"
print(s[5:12])
print(s[2:4])
print(s[-16:-14])
print(s[5:])

#reverse string
print(s[::-1])
print(s[::-2])
'''

#String Build in functions

#variable.build-in-function
b = "I am Praveen Kumar"
print(b)
print(b.upper())
b1=b.lower()
print(b)
print(b1)
print("am saravanan".capitalize())
print("i am sampritha from hcl".title())
print("JAVA".casefold())
print("Sugan".center(30,"*"))
print("Hello Mukil".swapcase())
print("Praveen Kumar".count("z"))
print("Praveen Kumar".startswith("Prai"))
print("Praveen Kumar".endswith("ar"))

print("Thirumalaivasan".index("i"))
print("Thirumalaivasan".rindex("i"))
print("Thirumilaivasan".index("i",3))

print("Nivetha".find("h"))
print("Nivitha".rfind("i"))

x = "I am {} from {}"
print(x)
print(x.format("AI Developer","Zoho"))

n = "Praveen"
print(f"i am {n}")


#Escape sequence
print("\n1.Apple\n2.Samsung\n3.Realme\n4.Oppo")

print("\n1.Apple\n2.Samsung\n3.Realme\n4.Oppo")
print("I\tam\tpraveen")


l = "Hello, I am Mukil, from TCS"
print(l)
l1 = l.split(",")
print(l1)
j = "-".join(l1)
print("j : ",j)


vj = "Mr.Vijay\nis\nChif Misister of\nTamilndau"
print(vj.splitlines())

vj.isdigit


#String based based
#1.reverse string
p = "python"
m = ""
#print(p[::-1])
for i in p:
    m=i+m

print(m)
"""
m = "p"+"" => "p"
m = "y"+"p" => "yp"
m = "t"+"yp" => "typ"
m = "h"+"typ" => "htyp"
m = "o"+"htyp" => "ohtyp"
m = "n"+"ohtyp" => "nohtyp"
"""
#2.remove duplicate character
s = "Praveen Kumar"
s1 = ""
for i in s:
    if i not in s1:
        s1+=i

print(s1)


#3.Find no of vowels sound in string data
s = "ThirumalivasAn"
c=0
for i in s:
    if i in "aeiouAEIOU":
        c+=1

print("No of vowles : ",c)






















