num=int(input("enter the number"))
sum=0
i=1
while i<num:
    if num%i==0:
        per=i
        sum=sum+per
    i=i+1
if num==sum:
    print(num,"is pefect number")
else:
    print(num,"is not perfect number" )