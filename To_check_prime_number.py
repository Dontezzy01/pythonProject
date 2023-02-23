#How to check a prime number
num=int(input("Enter a number: "))
Flag = False
if num == 1:
    print(num, "is not a PRIME NUMBER")
elif num > 1:
    for i in range (2,num):
        if num%i==0:
            Flag = True
            break
    if Flag:
        print(num,"is not PRIME NUMBER")
    else:
        print(num,"is a PRIME NUMBER")