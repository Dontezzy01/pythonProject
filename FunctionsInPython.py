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
print(result)

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