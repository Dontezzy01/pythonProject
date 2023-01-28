grade = int(input("Enter your score: "))

if (grade>=70):
    print("You're an excellent student")
elif (grade>=60 and grade<=69):
    print("Very good!")
elif (grade>=50 and grade<=59):
    print("You are an average student")
elif (grade>=40 and grade<=49):
    print("Passed!")
else:
    print("You have failed!")

print("Thank you for entering your grade")