number=int(input("Enter Number: "))
Digits=[12,23,90,21,43,33,44,98,80,14,13,17,2]
for num in Digits:
    if num == number:
        print("Number exist")
        break
    else:
        print("The number does not exist")
        break