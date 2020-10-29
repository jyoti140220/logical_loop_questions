i=1
sum=0
while i<=11:
    num=int(input("enter the wheight: "))
    sum=sum+num
    i=i+1
av=sum/11
print("average",av)
if av%5==0:
    print("avrage =",av, ",5 ka multiple h")
else:
    print("avrage =",av, ",5 ka multiple nhi h")



    