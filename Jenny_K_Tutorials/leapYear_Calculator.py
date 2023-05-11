# Function that that calculates whether a year is a leap year or not

year = int(input("Type in the year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"This year, {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")
    else:
        print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")