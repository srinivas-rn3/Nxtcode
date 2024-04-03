import datetime
from datetime import datetime,date, timedelta
import sys
import pandas as pd
import calendar
'''
p = pd.Period('2022-07-01')
p = p.days_in_month
print(p)
'''
'''
c = calendar.monthcalendar(2022,7)
print(c)
'''
'''
todayDate = datetime.date.today()
if todayDate.day > 25:
    todayDate += datetime.timedelta(7)
to = todayDate.replace(day=1)
print(to)
'''
# Get today's date
today = date.today().isoformat()
print("Today is: ", today)
# Yesterday date
#yesterday = (date.today() - timedelta(1)).isoformat()
#print("Yesterday was: ", yesterday)

#monday = (date.today() - timedelta(7)).isoformat()
## just to run manually
next_date = (date.today() + timedelta(7)).isoformat()
print("Last Monday's Date: ", next_date)


