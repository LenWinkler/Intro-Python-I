"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

date = datetime.now()
current_year = int(date.strftime("%Y"))
current_month = int(date.strftime("%m"))
cal = calendar.TextCalendar(firstweekday=0)
args = sys.argv

if len(args) == 1:
  print(cal.formatmonth(current_year, current_month))
  
elif len(args) == 2 and int(args[1]) <= 12:
  print(cal.formatmonth(current_year, int(args[1])))

elif len(args) == 3 and int(args[1]) <= 12:
  print(cal.formatmonth(int(args[2]), int(args[1])))

elif len(args) > 3 or int(args[1]) > 12:
  print('\nError. This program expects arguments in the following format: ** 14_cal.py [year] [month] **. If only one argument is provided, it will assume that the month has been specified and will print that month\'s calender for the current year. If no arguments are passed, it will print the current month.\n')



# python3 src/14_cal.py