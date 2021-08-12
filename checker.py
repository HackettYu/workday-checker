import datetime
from chinese_calendar import is_workday, is_holiday, is_in_lieu

# Fixed: timezone sub 16 hours cause UTC +8 in China
one_day_duration = datetime.timedelta(days=1)
today = datetime.date.today()
tomorrow = datetime.date.today() + one_day_duration

try:
    if tomorrow.weekday() in (5, 6) and is_workday(tomorrow):
        print(f'Tomorrow {tomorrow} is workday and weekend, do you hava set the alarm clock?') # noqa
    elif is_workday(today):
        print(f'Just work in {today}.')
    elif is_in_lieu(today):
        print(f'Today {today} is holiday but also lieu.')
    elif is_holiday(today):
        print(f'Today {today} is holiday, have a good day!')
except NotImplementedError:
        print('Please check chinese_calendar had updated and the date is invalid.') # noqa
