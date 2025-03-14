import datetime
import bday_messages


date_today = datetime.date.today()
next_bday = datetime.date(2025, 3, 13)

time_difference = next_bday - date_today

if next_bday == date_today:
    print(bday_messages.random_messages)
else:
    print(f'My next birthday is {time_difference} days away')
