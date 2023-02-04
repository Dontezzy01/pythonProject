Secret_num = 9

while True:
    guess = int(input("Guess a number from 1 to 10: "))

    if guess == Secret_num:
        print("You guessed the number")
        break
    else:
        print("You entered a wrong input")