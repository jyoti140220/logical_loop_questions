a=input("enter the chracter : ")
num=0
alpha=0
i=0
while i<len(a):
    if a[i]>="0" and a[i]<="9":
        num=num+1
    if a[i]>="a" and a[i]<="z":
        alpha=alpha+1
    i=i+1
print(num,"number")
print(alpha,"alphabate")