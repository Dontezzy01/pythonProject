#nums=[12,23,89,2,3,11]
#for num in nums:
 #   if num%5==0:
  #      print(num)
   #     break
#else:
 #       print("Not found")


nums=int(input("Enter a number: "))
Flag=False
if nums < 1:
    print("You entered a wrong digit")
elif nums == 1:
    print("Not a prime number")

elif nums>1:
    for i in (2,nums):
        if nums%i:
            flag=True
            break
    if Flag:
        print(nums, "is not a prime number")
    else:
        print(nums,"is a prime number")