import calendar
def leap_year(y):
  if calendar.isleap(y):
    print("is a leap year",y)
  else:
    print("is a leap year",y)
  y=int(input("enter a year:"))
  z=leap_year(y)
  print("The result is:",z)
  