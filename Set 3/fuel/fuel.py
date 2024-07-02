while True:
    try:
        x_input, y_input = input("Fraction: ").split(sep = "/")
        x_input = int(x_input)
        y_input = int(y_input)
        if x_input <= y_input:
            max_fuel = (x_input / y_input)
            break
    except (ValueError, ZeroDivisionError):
        pass

max_fuel = round(max_fuel * 100)

if max_fuel >= 99:
    print("F")
elif max_fuel <= 1:
    print("E")
else:
    print(max_fuel,"%", sep="")