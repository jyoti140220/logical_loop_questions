i=1
num=5
while i<=5:
        guess=int(input(" enter your guess: "))
        if guess==num:
           print("congress,you won")
           break
        elif guess!=num and i==5:
           print("your chance is over")
        elif guess!=num:
            print("try again")
        i=i+1
