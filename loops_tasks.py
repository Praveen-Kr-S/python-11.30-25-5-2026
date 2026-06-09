#jumping and transfewr statements
"""
1.break
2.continue
3.pass
"""
'''
#break
for i in range(10):
    if i==6:
        
        break
        
    print(i)


#continue
for i in range(10):
    if i==6 or i ==8:  
        continue   
    print(i)
'''
#pass
'''
i=1
while i<= 5:
    #print(i)
    #i+=1
    pass
'''






#Fibonacci series
#0,1
#0+1 = 1 +2+3+5+8+13

'''
n1 = 0
n2 = 1
for i in range(10):
    n3 = n1+n2
    print(n3)
    n1 = n2
    n2 =n3 
'''

#Plaindrome
"""
123 -> 321 -> not Plaindrome
121 -> 121 -> Plaindrome
"""
a = 121
b = 0
t = a

while t>0:
    d = t%10 # get the last digit of numbers
    b = b*10+d
    t = t//10 # remove the last digit of numbers

if b == a:
    print(f"{b} is palindrome")
else:
    print(f"{b} is not palindrome")

"""
1-> 121>0
d = 121 % 10 => d=1
b = 0*10+1 b=1
t = 121//10 => t=12

2-> 12>0
d = 12 % 10 => d=2
b = 1*10+2 b=12
t = 12//10 => t=1

3-> 1>0
d = 1 % 10 => d=1
b = 12*10+1 b=121
t = 1//10 => t=0

4 -> 0>0 ->False

"""

#12 Armstrong
#153 => 1**3 + 5**3 + 3**3 => 153
'''
a = int(input("Enter the vale : "))
b = 0
t = a
while t>0:
    d = t%10 #1
    .53
    t = t//10 # remove the last digit of numbers

if b == a:
    print(f"{b} is Armstrong")
else:
    print(f"{b} is not Armstrong")
'''















































































