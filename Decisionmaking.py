num=int(input("Enter a number: "))
if (num%2==0):
    if  (num%3==0):
        print("divisible by 2 and 3")
    else:
        print("divisible by 2 not 3")

else:
    if(num%3==0):
        print("divisible by 3 not 2")
    else:
        print("Not divisible by 3 and 2")