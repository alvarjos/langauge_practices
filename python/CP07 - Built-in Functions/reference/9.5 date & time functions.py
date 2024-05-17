# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################


from datetime import datetime, timezone
# datetime is part of the python standard library. 
# this one is kind of dumb because the name of the module is called "datetime" but then that module has a class (which we haven't learned about)
# also called "datetime". So you are saying "from the module called datetime, import the class datetime that has all those functions I want."




# two ways of getting the date and time:
print("now() function: ", datetime.now())
print("today() function:", datetime.today(), "\n")

# they are the same except that now() allows you to specify a specific time zone
# today() just always gives the current timezone of your computer

print("now() with UTC timezone", datetime.now(timezone.utc), "\n\n")


#let's store the datetime in a variable:
dateTimeExample = datetime.now()

# you can access any specific part of the time:
print("year", dateTimeExample.year)
print("month", dateTimeExample.month)
print("day", dateTimeExample.day)
print("hour", dateTimeExample.hour)
print("minute", dateTimeExample.minute)
print("second", dateTimeExample.second)
print("microsecond (millionths of seconds)", dateTimeExample.microsecond)

# strftime() or "string format time" function. Put it into more readable formats:
# we dont have time to show them all, but see chapter 9.5 for more examples:

print("\n\nstrftime() example:", dateTimeExample.strftime("%A %B %d"), "\n\n")


# strptime() or "string parse time" function.
# when you want to create a datetime object from a string.
# you need to give it a date as a string, and another string that tells how it is formatted:

dateString = "2023-09-26 14:45:08"
formatString = "%Y-%m-%d %H:%M:%S"

datetimeObj = datetime.strptime(dateString, formatString)
print("datetime created from a string:", datetimeObj)  # Outputs: 2023-09-26 14:45:08
print("see, it created a datetime object:", type(datetimeObj))  # Outputs: <class 'datetime.datetime'>

# you can give it different formats, the format string just has to match it:
dateString = "2023/09/26"
formatString = "%Y/%m/%d"

datetimeObj = datetime.strptime(dateString, formatString)
print("\nnotice it that the seconds are 00:00:00", datetimeObj)  
print("see, it created a datetime object:", type(datetimeObj))


# you can also create a datetime like this:
datetimeObj = datetime(2021, 10, 22)
print("\n\nmade with datetime() function", datetimeObj)