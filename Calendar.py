import calendar

#Value initialization
month_number = 0

#Greeting
print("Welcome To The Calendar Creator!!!")
#Starting date request
starting_day = str(input("Enter the name of the day you´d like your calendar to start with: "))
#Starting date actual assignment
if starting_day.lower() == "monday":
    calendar_ = calendar.TextCalendar(calendar.MONDAY)
elif starting_day.lower() == "tuesday":
    calendar_ = calendar.TextCalendar(calendar.TUESDAY)
elif starting_day.lower() == "wednesday":
    calendar_ = calendar.TextCalendar(calendar.WEDNESDAY)
elif starting_day.lower() == "thursday":
    calendar_ = calendar.TextCalendar(calendar.THURSDAY)
elif starting_day.lower() == "friday":
    calendar_ = calendar.TextCalendar(calendar.FRIDAY)
elif starting_day.lower() == "saturday":
    calendar_ = calendar.TextCalendar(calendar.SATURDAY)
elif starting_day.lower() == "sunday":
    calendar_ = calendar.TextCalendar(calendar.SUNDAY)
else:
    print("Option Unavailable")

#Month Selection
month_selection = str(input("Enter the name of the desired month you´d like to print: "))
#Loop to assign the month number
#Couln't use a dictionary since it must be referenced later
if month_selection.lower() == "january":
    month_number = 1
elif month_selection.lower() == "february":
    month_selection = 2
elif month_selection.lower() == "march":
    month_selection = 3
elif month_selection.lower() == "april":
    month_selection = 4
elif month_selection.lower() == "may":
    month_selection = 5
elif month_selection.lower() == "june":
    month_selection = 6
elif month_selection.lower() == "july":
    month_selection = 7
elif month_selection.lower() == "august":
    month_selection = 8
elif month_selection.lower() == "september":
    month_selection = 9
elif month_selection.lower() == "october":
    month_selection = 10
elif month_selection.lower() == "november":
    month_selection = 11
elif month_selection.lower() == "december":
    month_selection = 12
else:
    print("Option Unavailable")

year_selection = int(input("Enter the desired year of the calendar you'd like to print: "))
print("")

if month_selection >= 1 and month_selection <= 12:
    final = calendar_.formatmonth(year_selection, month_selection)
    print(final)
