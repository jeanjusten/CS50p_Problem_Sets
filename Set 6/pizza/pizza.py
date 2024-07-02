import csv
import sys
from tabulate import tabulate

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                pizza_dict = csv.DictReader(file)
                print(tabulate(pizza_dict, headers="keys", tablefmt="grid"))

        except FileNotFoundError:
                sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")