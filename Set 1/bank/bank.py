greeting = input("Greeting: ").title().strip()

# If the greeting starts with “hello”, output $0
if greeting.startswith("Hello"):
    print("$0")
# If the greeting starts with an “h” (but not “hello”), output $20
elif greeting.startswith("H") and greeting != "Hello":
    print("$20")
# Else, output $100
else:
    print("$100")
