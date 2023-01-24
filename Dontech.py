#This following program show the money invested and interest rate in 10 years
money = input("How much will you invest: ")
interest_rate = input("Enter your interest rate: ")
money = float(money)
interest_rate = float(interest_rate) * .01
for i in range(1,10):
    money = money + (money * interest_rate)
    print("The invested funds after 10yrs will be {:.2f}".format(money))