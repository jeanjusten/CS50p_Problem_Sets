import sys

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1].lstrip(),"r") as file:
                lines = file.readlines()
                counter = 0

                for l in lines:
                    if l.rstrip() and not l.lstrip().startswith("#"):
                        counter += 1
                print(counter)

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
