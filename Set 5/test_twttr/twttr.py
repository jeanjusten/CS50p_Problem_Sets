# Prompts the user for the name of a variable in camel case
def main():
    word = (input("Input: "))
    print(shorten(word))

# Outputs the corresponding name in snake case
def shorten(word):
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    words_list = []

    for c in word:
        if c not in vowels:
            words_list.append(c)
    return ''.join(words_list)

if __name__ == "__main__":
    main()

