# Prompts the user for an arithmetic expression and then calculates and outputs
expression = (input("Expression: ")).strip()
x, y, z = expression.split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(float((x+z)))
elif y == "-":
    print(float((x-z)))
elif y == "/":
    print(float((x/z)))
elif y == "*":
    print(float((x*z)))

