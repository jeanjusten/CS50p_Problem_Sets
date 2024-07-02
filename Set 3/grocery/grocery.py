item_list = {}

while True:
    try:
        item_input = input().upper()
        if item_input in item_list:
            item_list[item_input] = item_list.get(item_input) +1
        else:
            item_list[item_input] = 1
    except KeyError:
        pass
# until the user inputs control-d
    except EOFError:
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
        for i in sorted(item_list):
            print(item_list[i], i)

        quit()