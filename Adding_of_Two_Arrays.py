from numpy import*
numArr1 = array([12,34,23,78,90,13,80])
numArr2 = array([2,13,4,9,7,9,44])
numArr3=([])
k=0
for num1 in numArr1:
    num3= num1 + numArr2[k]
    numArr3.append(num3)
    k +=1
    print(numArr3)