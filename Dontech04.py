while True:

    try:
        Number = int(input("Enter a new number: "))
        break

    except ValueError:
        print("You didnt enter a number")

    except:
        print("An unknown number occurred")


print("Thank you for entering a number")