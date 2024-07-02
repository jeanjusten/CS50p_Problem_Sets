import random

def main():
    user_num = get_level()
    questions = 10
    global score
    score = 10

    while questions <= 10 and questions > 0:
        generate_integer(user_num)
        questions = questions - 1

    print("Score:", score)

# Prompts the user for a level, N . If the user does not input 1, 2, or 3, the program should prompt again.
def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input == 1 or user_input == 2 or user_input == 3:
                return user_input
            else:
                raise ValueError
        except ValueError:
            pass

# Randomly generates ten (10) math problems
def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    chances = 2

    while True:
        problem = int(input(f"{x} + {y} = "))
        answer = (x + y)

        try:
            if problem == answer:
                chances = 2
                break

            elif problem != answer and chances > 0:
                print("EEE")
                chances = chances - 1

            elif problem != answer and chances <= 0:
                print("EEE")
                print(f"{x} + {y} = {answer}")
                global score
                score = score -1
                break

        except ValueError:
            pass

if __name__ == "__main__":
    main()
