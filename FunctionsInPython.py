def greet():
    print("Good morning, Dontezzy!")
    print("I hope you are doing well!")
greet()


def add(a,b):
    c = a + b
    return c

result = add(9,3)
print(result)

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1, result2 = add_sub(10,8)
print(result1, result2)

def don_interest(principal,time, rate):
    I = principal*time*rate
    I = I*100
    return I
result = don_interest(900,12,34)
print("interest= ", result)

def update(x):
    x = 8
    print(id(x))
    print("x: ", x)
a = 10
update(10)
print(id(a))
print("a: ", a )

#Types of argument:
#Formal argument
#Actual argument

#Actual argument - position, keyward, default and variable length argument

#Postional argument: e.g.
def person(name,age):
    print(name)
    print (age)
person("Tezzy",22)

#Keyword argument: e.g.
def person(name, age):
    print(name)
    print(age)
person(age = 24, name = "Quadri")

#Default argument: e.g.
def person(name, age=19):
    print(age)
    print(name)
person("Dolapo")

#Variable length argument: e.g.
def add(a, *b):
    c= a
    for i in b:
        c=c+i
        print(c)
add(12,10,19,20)

#Keywords variable length argument(Kwargs)
def person(name,**data):
    print(name)
    print(data)


person("Dontezzy", age = 22, city = "Ibadan", phone = 903441384)
#or
#To print in a seperate way
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)


person("Dontezzy", age = 22, city = "Ibadan", phone = 903441384)

#def input_vals(name,**Age):
#    name= input(int("Enter your fullname"))
#    Age = input(int("How old are you"))
#    greetings = print("Best of luck, thanks")
#    print(name)
#    print(Age)
#    print(greetings)
#input_vals(name)

#Scope of variable
#-Local variable
#-Global variable

#-Local variable e.g.
def variable():
    x = 12
    print(x)
variable()

#-Global variable e.g.
x = 40
def values():
    #global x
    x = 12
    #globals()
    c = globals()['x']
    globals()['x'] = 20
    print("inside variable", x)
values()

print("outside variable: ", x)

#Passing list to a function e.g.
def count(list):
    even = 0
    odd = 0
    for i in list:
        if i&2==0:
            even+=1
        else:
            odd+=1
    return even, odd

list= [12,13,19,1,20,22,14,17,8,9,4,2,7]
even, odd= count(list)
#count(list)
print("Even= {} and Odd= {}".format(even,odd))

# Another example

#Take 10 name from from the user, count and display the number of user who has length more than five letters

def user(names):
    count = 0
    for name in names:
        if len(name) > 5:
            count += 1
    return count

names =["Aishat", "Quadri", "Ola", "Balikis", "Dolapo", "kareemot", "Sulaykoh", "Tayo", "Enny", "Ayomide"]
count = user(names)
print("Number of names with more than five letters: ",count)

#fabonacci sequence
def fab(n):
    a = 0
    b = 1
    print(a)
    print(b)
    if n < 0:
        print("You entered a wrong number")
    elif n == 1:
        print(a)
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fab(10)

print()

# Factorial number
def fact(x):
    factorial = 1
    for i in range(1,x+1):
        factorial = factorial * i
    return factorial
x=4
result = fact(x)
print(result)

