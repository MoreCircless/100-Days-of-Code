# import smtplib

# # * SMTP: Simple Mail Transfer Protocol

# connection = smtplib.SMTP("")
# connection.starttls()
# connection.login()


import datetime as dt



current_time = dt.datetime.now()
year = current_time.year
minute = current_time.minute
day_of_week = current_time.weekday()
print(current_time)
print(year)
print(minute)
print(day_of_week)

date_of_birth = dt.datetime(year=2001, day=5, month=12, hour=12)

print(date_of_birth)
