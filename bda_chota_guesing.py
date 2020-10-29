i=1
num=5
while i<=5:
    guess=int(input("enter the guess number: "))
    if guess==num:
        print("congress")
        break
    elif i==5 and guess>num:
        print("apka chnace khtam")
    elif i==5 and guess<num:
        print("apka chnce khtm")
    elif guess>num:
        print("your guess number is a large , try again")
    elif guess<num:
        print("your guess number is small , try again")
    i=i+1
    