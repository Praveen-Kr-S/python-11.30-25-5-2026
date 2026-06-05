"""
for loop
-- integer
1.increment for loop
2.decrement for loop
3.nested for loop
4.for loop usings strings and core-datatype
"""

#menbership oparator
#in/not in
"""
x=[1,2,3,4,5]
print(1 in x)
print(10 in x)
print(10 not in x)
print(3 not in x)
"""

#1.increment for loop

"""
        1     2                      4 
for vairable in range(start,stop,step[inc/dec]):
        3
    //looping statement
"""

#inc -> stop (n-1)
'''
#   1  2           4
for i in range(1,11,1):#12345
    #3
    print(i)
'''
"""
i=1
1 in 12345 ->T
i=1+1 = 2
i=2
2 in 12345 ->T
i=2+1 = 3
i=3
3 in 12345 ->T
i=3+1 = 4
i=4
4 in 12345 ->T
i=4+1 = 5
i=5
5 in 12345 ->T
i=5+1 = 6
i=6
6 in 12345 ->False
"""

'''
for i in range(1,10):
    print(i)

for i in range(10):
    print(i)
'''

#dec ->stop(n+1)
"""
for i in range(5,0,-1):#54321
    print(i)
    #5
    #4
    #3
    #2
    #1
"""

# for loop using string
'''
name = "Mukilleswar"
for i in name:
    print(i)
'''
'''
for i in "Python":
    print(i,end=" ")
'''

'''
#Nested Pattern

for i in range(5):#i=01234
    for j in range(5):#j=01234
        print("#",end=" ")
    print()
    
"""
i = 0
j = 01234

i = 1
j = 01234
"""


print("********************")
#inc pattern or half pyramid

for i in range(5):
    for j in range(i+1):
        print(j,end=" ")
    print()
"""
i = 0
j in range(0+1=1)->0
j = 0 -> T, j = 1 => F
i = 1
j in range(1+1=2)->01
j = 0 1 -> T, j = 2 => F
i = 2
j in range(2+1=3)->012
j = 0 1 2, j = 3 => F
i = 3
j in range(3+1=4)->0123
j = 0 1 2 3, j = 4 => F
i = 4
j in range(4+1=5)->01234
j = 0 1 2 3 4, j = 5 => F
i = 5 -> Fasle
"""
print("********************")
#dec pattern or inverted half pyramid

n = 5
for i in range(n):
    for j in range(i,n):
        print(j,end = " ")
    print()
print("********************")

#full pyramid

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end = " ")

    for j in range(i+1):
        print("*",end=" ")

    for j in range(i):
        print("*",end=" ")
    print()

print("--------------------------")
#Inverted full pyramid

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end = " ")

    for j in range(i,n):
        print("*",end=" ")

    for j in range(i,n-1):
        print("*",end=" ")
    print()

#Hollow Pattern

n = 5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()

print("--------------------------")

for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()


print("--------------------------")
#HOLLOW SQUARE
for i in range(n):
    for j in range(n):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("--------------------------")

#plus pttern

for i in range(n):
    for j in range(n):
        if i == 2 or j == 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("--------------------------")

#cross pttern

for i in range(n):
    for j in range(n):
        if i == j or i+j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("--------------------------")

#Hollow square with assci values

c = 65
for i in range(n):
    for j in range(n):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*",end=" ")
        else:
            print(chr(c),end=" ")
            c+=1
    print()

'''


#while loop
'''
syntax of while loop

 1
variable-setup
        2
while condition:
        3
    #looping statement
        4
    #inc/dec

1.inc while
2.dec while
3.infinite loop
'''


#inc
'''
i = 1
while i<=5:
    print(i)
    i+=1

print("--------------------------")
#dec

i = 10
while i>=6:
    print(i)
    i-=1

#infinite loop
#1.based on condition true



i = 10
while True:
    print(i)
    i-=1


#2.based on inc/dec

i = 10
while i>=6:
    print(i)
    i+=1
'''

#factorial
#5 => 5*4*3*2*1 = 120

v = int(input("Enter the value :"))
f = 1
for i in range(1,v+1):
    f=f*i


print("Factorial : ",f)
"""
i=1 => f = 1*1 = 1
i=2 => f = 1*2 = 2
i=3 => f = 2*3 = 6
i=4 => f = 6*4 = 24
i=5 => f = 24*5 = 120
"""


