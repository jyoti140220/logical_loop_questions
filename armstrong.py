num=int(input("enter the number"))
sum=0
i=1
v=num
while num>=i:
    x=num%10
    y=x**3
    sum=sum+y
    num=num//10
print(sum)
if v==sum:
    print("it is armstrong number")
else:
    print("not armstrong number")