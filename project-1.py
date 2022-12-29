print("Number Guessing Game")
i=0
chances=5
for i in range(0,9):
    print("Guess any Number between 1 and 9")
    Guess=int(input("ENter your guess"))
    if Guess == 9:
        print("Congratulation YOU WON!!!")
        break
    else:
        chances-=1
        print("Your guess was too low: Guess a number higher than or equal to  ",Guess+1)
    
