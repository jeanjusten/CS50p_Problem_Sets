import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    match = re.match(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$",ip)

    if match:
        gp_1 = int(match.group(1))
        gp_2 = int(match.group(2))
        gp_3 = int(match.group(3))
        gp_4 = int(match.group(4))

        if gp_1 >= 0 and gp_1 <= 255 and gp_2 >= 0 and gp_2 <= 255 and gp_3 >= 0 and gp_3 <= 255 and gp_4 >= 0 and gp_4 <= 255:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()