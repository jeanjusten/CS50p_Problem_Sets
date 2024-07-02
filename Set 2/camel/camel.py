# Prompts the user for the name of a variable in camel case
variable_camel = input("camelCase: ")

# Outputs the corresponding name in snake case
for c in variable_camel:
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.lower(), end="")
