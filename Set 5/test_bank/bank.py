def main():
    greeting = input(str("Greeting: ")).title().strip()
    greeting_value = int(value(greeting))
    print(f"${greeting_value}")

def value(greeting):

    if greeting.startswith("Hello"):
        return 0

    elif greeting.startswith("H") and greeting != "Hello":
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()
