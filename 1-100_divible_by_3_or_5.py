for i in range(1,100):
    if i%3==0 and i%5==0:
        continue
    print(i,end=" ")


#for letter in "Communication":
 #   if letter=="m":
  #      pass
   #     print("It has been ommitted intentionally")
    #print("lines- ", letter)


list=[1,2,3,8,9,7]
Tezzy=iter(list)
print(next(Tezzy))


for i in Tezzy:
    print(i, end=" ")
    print()

#import sys
#while True:
 #   try:
  #      print(next(Tezzy))
   # except StopIteration:
      #  sys.exit()
