# Prompts the user for the name of a variable in camel case
vowels = ["A","a","E","e","I","i","O","o","U","u"]
word = (input("Input: "))

for c in word:
    if c not in vowels:
        print(c, end ="")