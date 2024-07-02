def main():
# Prompts the user for a time
    time = input("What time is it? ")

# Outputs
# Breakfast time
    if 7 <= convert(time) <= 8:
        print("Breakfast time")
# Lunch time
    elif 12 <= convert(time) <= 13:
        print("Lunch time")
# Dinner time
    elif 18 <= convert(time) <= 19:
        print("Dinner time")

# Defining convert time function
def convert(time):
    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)
    minutes = round(minutes/60, 2)
    return (hours + minutes)

# Run the program
if __name__ == "__main__":
    main()