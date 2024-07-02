def main():
    user_input = input("Input: ")
    converted = emoji(user_input)

    print(converted)

def emoji(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

main()