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
print("**********")
#dec pattern or inverted half pyramid

n = 5
for i in range(n):
    for j in range(i,n):
        print(j,end = " ")
    print()






































