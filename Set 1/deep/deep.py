userGuess = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").title().strip()

match userGuess:
    case "42" | "Forty-Two" | "Forty Two":
        print("Yes")
    case _:
        print("No")
