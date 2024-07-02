import inflect
names_list = []
p = inflect.engine()

while True:
    try:
        user_input = input("Input: ")
        names_list.append(user_input)
    except EOFError:
        if len(names_list) == 1:
            print("Adieu, adieu, to", names_list[0], end="\n")
        else:
            names_conv = p.join((names_list))
            print("Adieu, adieu, to", names_conv)
        break