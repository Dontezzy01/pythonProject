principal=float(input("Enter your principal: "))
rate=float(input("Enter yout rate: "))
time=int(input("Enter your time: "))
interest = float(principal*rate*time)
interest = (interest/100)*.01
Amount = float(principal+interest)
print("Interest= ",interest)
print("Amount= ",Amount)
for i in range(1,10):
    payup = Amount + principal
    print("The amount in the next {} year(s) is {}".format(i,payup))
print("The calculation was done successfully")
