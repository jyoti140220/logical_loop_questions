num1=int(input("enter thr 1st number"))
num2=int(input("enter the 2nd number"))
i=1
while i<=num1 and i<=num2:
    if num1%i==0 and num2%i==0:
        hcf=i*1
    i=i+1
print(hcf)