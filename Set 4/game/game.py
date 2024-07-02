import random

while True:
    try:
        user_input = int(input("Level: "))
        if user_input > 0:
            rgn = random.choice(range(1,user_input))
            break
    except ValueError:
        pass

while True:
    try:
        user_guess = int(input("Guess: "))
        if user_guess > rgn:
            print("Too large!")
        elif user_guess < rgn:
            print("Too small!")
        else:
            print("Just right!")
            quit()

    except ValueError:
        pass