principal=float(input("Enter your principal: "))
rate=float(input("Enter yout rate: "))
time=int(input("Enter your time: "))
interest = float(principal*rate*time)
interest = (interest/100)*.01
Amount = float(principal+interest)
print("Interest= ",interest)
print("Amount= ",Amount)
for i in range(1,10):
    Amount = Amount + (principal + 1000)
    print("The amount in the next {} year(s) is {}".format(i,Amount))
print("The calculation done successfully")
