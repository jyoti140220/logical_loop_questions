num=int(input("enter the number"))
y=num
sum=0
i=1
while num>=1:
    x=num%10
    sum=sum+x
    num=num//10
if y%sum==0:
    print(y,"it is harshad number")
else:
    print(y,"it is not harshad number")