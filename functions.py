
"""
1.predefined functions
2.user defined functions
3.return type functions
4.lambda functions
5.recursive functions

2.user drfined functions
    1.without argument functions
    2.with argument functions
        1.positional argument function
        2.default argument function
        3.keyword argument function
        4.variable argument function or orbitary function

syntax of function
function define
def function_name():
    #block of code

function_call
function_name()
"""
#1.without argument functions
def fire():
    print("fire mode is on...")

# fire()
# fire()
# fire()

# 2.with argument function // positional argument function
def add(x,y):
    a = x
    b = y
    c = a + b
    print("Add Value :",c)

# add(10,4)
# add(10,6)


#default argument function
def concat(fn="Praveen",ln="Kumar"):
    print(f"Full Name :{fn} {ln}")

# concat()
# concat("Ramesh")
# concat("Ramesh","Babu")


# 3.Keyword arguments function ->**variable
"""
def function_name(**variable):
    #block of code
    
function_call()
"""

def info(**d):
    print(d)
    print(type(d))
    for k,v in d.items():
        print(k,":",v)

# info(name="Praveen",age=2,city="Salem")
# info(name="Sugavaneswar",age=3,city="Chennai")

# 4 variable argument function
"""
def function_name(*variable):
    #block of code

function_call()
"""
def std_name(*t):
    print(t)
    print(type(t))
    for i in t:
        print(i)

# std_name("Praveen","Saravanan","Sugavaneswar","Nivetha","Mukilleswar")




#function task
def remove_duplicates(l):
    v = []
    for i in l:
        if i not in v:
            v.append(i)
    print(v)
remove_duplicates([34,5,6,34,5,23,46,34,9])

