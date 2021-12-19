import calendar

month_selection = str(input("Enter the name of the desired month you´d like to print: "))
year_selection = int(input("Enter the year of the desired month you'd like to print: "))
print("")
month_format = month_selection.lower()
month = {
    {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6", "july": "7",
     "august": "8", "september": "9", "october": "10", "november": "11", "december": "12"}
}
calendar_ = calendar.TextCalendar(calendar.MONDAY)
str = calendar_.formatmonth(int(year_selection), int(month[month_format]))
print(str)
