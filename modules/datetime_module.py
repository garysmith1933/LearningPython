import datetime
# args = hours, minute
mytime = datetime.time(2, 20)
print(mytime.hour, mytime.minute)
print(mytime)

today = datetime.date.today() # prints 2023-02-07
print(today)
print(today.ctime())

from datetime import datetime

mydatetime = datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime)

# DATE
from datetime import date

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
res = date1 - date2
print(res)

# DATE TIME
datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)

res = datetime1 - datetime2
print(res) # can print days and seconds apart using .days / .seconds