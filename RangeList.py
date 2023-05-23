fruits=["Banana","Pawpaw","Apple","Pineapple","Orange","Carrot"]
for fruit in fruits:
    print("This fruit is ", fruit)
print()
for letters in "Python":
    print("current letter is: ", letters)

fruits=["Banana","Pawpaw","Apple","Pineapple","Orange","Carrot"]
for index in range(len(fruits)):
    print("fruits: ",fruits[index])
print()


number=[17,37,93,37,89,79,17,3,7,77]
for num in number:
    if num%2==0:
        print("The even number: ", num)
        break
    else:
        print("The odd number: ", num)
        continue



for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(k, end="  ")
    print()