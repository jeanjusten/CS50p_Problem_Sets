# Prompts the user to insert a coin one at a time, each time informing the user of the amount due
def main():
    due = 50
    while due > 0:
        print("Amount Due:", due)
        due = (due - get_coin())
    else:
        due = int(due)
        (print("Change Owed:", abs(due)))

def get_coin():
    coin = int(input("Insert Coin: "))
    if coin == 10 or coin == 25 or coin == 5:
        return coin
    else:
        return 0

main()




