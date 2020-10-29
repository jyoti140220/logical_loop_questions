a=input("enter the number")
if a>="65" and a<="90":
    print(chr(int(a)))
elif a<="97" and a<="122":
    print(chr(int(a)))
elif a>="a" and a<="z":
    print(ord(a))
elif a>="A" and a<="Z":
    print(ord(a))