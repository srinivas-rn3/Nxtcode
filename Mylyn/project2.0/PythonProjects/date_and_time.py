import datetime 

'''
Getting the Current Date and Time
You can get the current date and time using the datetime class:

'''
current_date = datetime.datetime.now()

print(current_date)

'''
Creating a Specific Date and Time
You can create a specific date and time using the datetime class constructor:
'''
specific_datetime  = datetime.datetime(2024,3,12,15,30,0)
print(specific_datetime)
'''
Formatting Dates and Times
You can format dates and times using the strftime() method, which stands for
"string format time". Here are some common format codes:

%Y: Year (4 digits)
%m: Month (2 digits)
%d: Day of the month (2 digits)
%H: Hour (24-hour clock, 2 digits)
%M: Minute (2 digits)
%S: Second (2 digits)

'''
formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S") 
print(formatted_datetime)

'''
Parsing Dates and Times from Strings
You can also parse dates and times from strings using the strptime() method:

'''
date_string = "2024-03-12"
parsed_date = datetime.datetime.strptime(date_string,"%Y-%m-%d")
print(parsed_date)

'''
Working with Time Differences
You can perform arithmetic operations on dates and times to calculate time differences:

'''
delta = specific_datetime - current_date 
print(delta.days) # Number of days
print(delta.seconds) # Number of seconds (excluding days)

'''
When you subtract one datetime object from another,
Python automatically creates a timedelta object 
representing the difference in time between the two datetime objects.
'''


'''
Adding or Subtracting Time
You can add or subtract time from a datetime object using timedelta objects:

'''
current_date1 = datetime.datetime.now()
print("Current Date : ",current_date1)

one_day = datetime.timedelta(days=1)
one_week = datetime.timedelta(weeks=1)

new_datetime = current_date1 + one_day 
print("Date time one day later : ",new_datetime)

new_datetime_week = current_date1 + one_week
print("Date time one week later : ", new_datetime_week)

new_datetime_minus_day = current_date1 - one_day
print("Date time one day earlier : ",new_datetime_minus_day )