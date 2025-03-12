import random
guess= random.randint(1,10)
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess_count+=1
    enter = int(input("enter: "))
    if enter>guess:
        print("higher")
        guesses_left=3-guess_count
        print(f"{guesses_left} guesses left")
    elif enter<guess:
        print("lower")
        guesses_left=3-guess_count
        print(f"{guesses_left} guesses left")
    elif enter==guess:
        print("correct")
        break
        
        

