import calendar
m = list(calendar.month_name)
m.pop(0) #remove the empty value

def is_leap(year):
  """Takes a specific year and checks to see if it is leap year by checking it is divisible by 400."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
is_leap()

def days_in_month(year, month):
  """Takes the month that you have chosen from the year you have checked previously and prints
  out the number of days in that month."""
  month_days = [31, 28, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31]
  months = []
  if is_leap(year) and month == 2:
    return "29"
  else:
    return month_days[month-1]
days_in_month()  
year = int(input("Enter a year: ")) # User inputs a year
month = int(input("Enter a month: ")) # User inputs a month
days = days_in_month(year, month)
print(f"There are {days} days in {m[month]} {year}.")