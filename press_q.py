count=0
product=1
sum=0
i=1
while True:
    num=str(input("enter num"))
    if num=="q":
        break
    sum=sum+int(num)
    count=count+1
    product=product*int(num)
print("avrage : ",sum/count)
print("product : ",product)