
#Firstnum=23
#Secondnum=89
#Thirdnum=23

Firstnum=int(input("Enter your first nunber: "))
Secondnum=int(input("Enter your second number: "))
Thirdnum=int(input("Enter your third number: "))
if (Firstnum >= Secondnum) and (Firstnum >= Thirdnum):
    largest = Firstnum
elif (Secondnum >= Firstnum) and (Secondnum >= Thirdnum):
    largest = Secondnum
else:
    largest = Thirdnum
print("The largest number is ", largest)
print("Thamk you for entering digits, Bye.")