def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if ( 6 >= len(s) >= 2): # Checking if the array lenght is between 2 and 6 characters
        if s.isalpha(): # If the plate is all letters, then its automatically valid
            return True

        # If the plate is not all letters, then it must be alpha-numeric and have the first two characters as Letters
        elif s.isalnum() and s[0:2].isalpha():
            for char in s: # Making a loop in the plate and calling its characters "char"
                if char.isdigit(): # Checking if the looped character "char" is a number
                    position = s.index(char)  # Storing the number in the variable called position with .index()

                    if s[position:].isdigit() and int(char) != 0: # Checking if anything that comes after the digit is a number and if the first digit is not 0
                        return True
                    else:
                        return False
                    
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()