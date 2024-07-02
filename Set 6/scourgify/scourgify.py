import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1],"r") as before:
            before_info = csv.DictReader(before) # read the info in the first file
            list = []

            for line in before_info: # Looping through before_info dict and setting up keys to the new list
                surname, name = line["name"].split(",")
                name = name.lstrip()
                house = line["house"]
                list.append({"first":name,"last":surname,"house":house}) # Append the info from the first file to a list variable and declaring fieldnames as headers

            with open(sys.argv[2], "w") as after_info: # with the second file open
                after = csv.DictWriter(after_info, fieldnames=["first","last","house"]) # writing the info on the second file
                after.writeheader() # you can tell a DictWriter to write its fieldnames to a file using writeheader with no arguments
                for row in list:
                    after.writerow(row) # adding every line of the list variable to the second file, using the fieldnames declared before

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
