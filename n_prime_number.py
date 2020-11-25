a=int(input("enter the number :"))
i=2
c=0
b=0
while True:
    c=c+1
    j=2
    while j<i:
        if i%j==0:
            break
        j=j+1
    else:
        b=b+1
        print(i)

    i=i+1
    if c==b:
        break