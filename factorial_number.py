num=int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Sorry, Factorial does not support negative number")
if num == 0:
    print("The factorial of 0 is", factorial)
else:
    for i in range(1,num+1):
        factorial= factorial*i
    print("The factorial of ",num,"is", factorial)