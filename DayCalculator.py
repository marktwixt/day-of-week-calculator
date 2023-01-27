def day_of_week(year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    return (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
year = int(input("Enter year (YYYY): "))
month = int(input("Enter month (MM): "))
day = int(input("Enter day (DD): "))

print("The day of the week is:", days[day_of_week(year, month, day)])

# This program uses a mathematical formula to calculate the day of the week. 
# The algorithm is based on the fact that the number of days between two dates is the difference between their Julian Day Numbers (JDN). 
# The JDN for any date can be calculated using the following formula:
# JDN = (1461 * (year + 4800 + (month - 14) // 12)) // 4 + (367 * (month - 2 - 12 * ((month - 14) // 12))) // 12 - (3 * ((year + 4900 + (month - 14) // 12) // 100)) // 4 + day - 32075
# The day of the week can then be calculated by taking the JDN modulo 7.
# In this program, I use a lookup table t to store the number of days from the beginning of the year 
# to the first day of the month, and then use the formula to calculate the day of the week, then use the result mod 7 to get the index of days of the week which is then printed out.
# Please note that this algorithm is valid only for dates after the adoption of the Gregorian calendar (1753 in the UK, 1582 in most of the Catholic countries)