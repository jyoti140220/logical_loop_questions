num=int(input("enter the numbe : "))
count1=0
count2=0
i=1
while i<=num:
    if num%2==0:
        count1=count1+1
    else:
        count2=count2+1
    num=num//10
print(count1,"even")
print(count2,"odd")
