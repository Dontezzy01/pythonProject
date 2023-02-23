i=0
while i<=10:
    print("#", end="")
    j = 0
    while j <= 8:
        print("#", end="")
        j+=1
    i+=1
    print()


for i in range(1,4):
            for j in range(1,4):
                print("I am Don", end="")
                print("Tezzy", end=" ")
                print()

for i in range(8):
    for j in range(i):
        print("#", end=" ")
    print()

print()


for i in range(8):
    for j in range(8-i):
        print("#", end=" ")
    print()



