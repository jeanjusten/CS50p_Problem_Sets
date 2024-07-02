import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if match:= re.search(r"^(([0-9]{1,2})(:{1}[0-5]{0,1}[0-9]{1})?)\s{1}(AM{1}|PM{1})\s{1}to{1}\s{1}(([0-9]{1,2})(:{1}[0-5]{0,1}[0-9]{1})?)\s{1}(AM{1}|PM{1})$",s):

        hour_1 = match.group(2)
        minutes_1 = match.group(3)
        hour_ampm = match.group(4)
        hour_2 = match.group(6)
        minutes_2 = match.group(7)
        hour_2ampm = match.group(8)

# 1st hour input
        if 1 <= int(hour_1) <= 12 and 1 <= int(hour_2) <= 12:
            if minutes_1 != None:
                n_minutes = minutes_1
            else:
                n_minutes = ":00"

            if hour_ampm == "AM":
                if int(hour_1) != 12:
                    first_hour = (f"{hour_1:>02}{n_minutes}")
                else:
                    first_hour = (f"00{n_minutes}")
            else:
                if int(hour_1) != 12:
                    n_hour1 = int(hour_1) + 12
                    first_hour = (f"{n_hour1:>02}{n_minutes}")
                else:
                    n_hour1 = int(hour_1)
                    first_hour = (f"{n_hour1:>02}{n_minutes}")

# 2nd hour input
            if minutes_2 != None:
                n_minutes2 = minutes_2
            else:
                n_minutes2 = ":00"

            if hour_2ampm == "AM":
                if int(hour_2) != 12:
                    second_hour = (f"{hour_2:>02}{n_minutes2}")
                else:
                    second_hour = (f"00{n_minutes2}")
            else:
                if int(hour_2) != 12:
                    n_hour2 = int(hour_2) + 12
                    second_hour = (f"{n_hour2:>02}{n_minutes2}")
                else:
                    n_hour2 = int(hour_2)
                    second_hour = (f"{n_hour2:>02}{n_minutes2}")

            return f"{first_hour} to {second_hour}"
        else:
            raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()