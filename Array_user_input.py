from array import*
Don=array("i",[])
num=int(input("Enter length of the array: "))
for i in range(num):
    x = int(input("Enter the next value: "))
    Don.append(x)
print(Don)

val=int(input("Enter value for search: "))
k=0
for e in Don:
    if e == val:
        print(k)
        break
    k+=1
    #or
print(Don.index(val))