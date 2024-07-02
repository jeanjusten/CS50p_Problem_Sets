month_list = [
    "0",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636
while True:
    user_input = input("Date: ")

    if user_input[0:1].isalpha():
        separator = ","
        if separator in user_input:
            monthDay, year = user_input.split(sep=",")
            month, day = monthDay.split(sep=" ")
            day = int(day)

            if month in month_list:
                month_wrt = str(month_list.index(month))
                if (day <= 31):
                    print(year.strip(),"-",month_wrt.rjust(2,'0'),"-",(f"{day:02}"), sep="")
                    break

    else:
        separator = "/"
        if separator in user_input:
            month, day, year = user_input.split(sep="/")
            month = int(month)
            day = int(day)
            if (month <= 12) and (day <= 31):
                print(year.strip(),"-",(f"{month:02}"),"-",(f"{day:02}"), sep="")
                break