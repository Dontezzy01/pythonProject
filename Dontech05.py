Secret_num = 9

while True:
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == Secret_num:
        print("You guessed the number")
        break
    else:
        print("You entered a wrong input")

count = 0

for _ in range(10):
    name = input("Enter a name: ")
    if len(name) > 5:
        count += 1

print("Number of names with more than five letters:", count)
