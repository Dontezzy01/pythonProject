#Recursion in Python
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i+=1
    print("Hello.... dontezzy", i)
    greet()
#greet()


#Factorial using Recursion

def fact(n):
    if n==0:
        return 1
    return(n * fact(n-1))

result = fact(7)
print(result)

#Anonymous Fucntion(Lambda in python)
f = lambda a : a*a
result = f(7)
print(result)
# or
f = lambda a,b : a+b
result = f(10,14)
print(result)

# lambda function can be used with these three function: filter(), map(), reduce()
# 1- Filter(): e.g.--- filter(func , iterable)
def is_even(n):
    if n%2==0:
        return n
nums=[4,3,2,7,8,9,8,12,43,80,34,44]
even=list(filter(is_even, nums))
result=even
print(result)

# used this instead(lambda function)
nums=[4,3,2,7,8,9,8,12,43,80,34,44]
evens=list(filter(lambda n : n%2==0, nums))
result=evens
print("filter--- Evens = ", result)

# 2- Map() : e.g.--- map(func , *iterable)
nums=[4,3,2,7,8,9,8,12,43,80,34,44]
doubles=list(map(lambda nums : nums*2, nums))
result= doubles
print("map--- Doubles = ", result)

from functools import reduce
# 3- Reduce() : e.g.--- reduce(func , iterable[,initial])
nums=[8, 6, 4, 14, 16, 18, 16, 24, 86, 160, 68, 88]
sum=reduce (lambda a,b: a+b, nums)
result = sum
print("reduce--- Doubles = ", result)
