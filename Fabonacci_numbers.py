#How to print  fabonacci number
nterms=int(input("How maany terms: "))
n1=0
n2=1
count=0
if nterms < 0:
    print("Please! Enter a positive number, you entered a wrong number!")
elif nterms==1:
    print("Fabonacci sequences is upto",nterms,":" )
    print(n1)
else:
    print("fabonacci sequemces: ")
    while count< nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
