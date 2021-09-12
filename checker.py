import datetime
from chinese_calendar import is_workday, is_holiday, is_in_lieu


one_day_duration = datetime.timedelta(days=1)


def day_checker(pivot: datetime.date) -> None:
    try:
        if pivot.weekday() in (5, 6) and is_workday(pivot):
            print(f'{pivot} is workday and weekend, do you have set the alarm clock?\n\r') # noqa
        elif is_workday(pivot):
            print(f'Just work in {pivot}.\n\r')
        elif is_in_lieu(pivot):
            print(f'{pivot} is holiday but also lieu.\n\r')
        elif is_holiday(pivot):
            print(f'{pivot} is holiday, have a good day!\n\r')
    except NotImplementedError:
            print('Please check chinese_calendar had updated and the date is invalid.\n\r') # noqa


if __name__ == "__main__":
    today = datetime.date.today()
    yesterday = today - one_day_duration
    tomorrow = today + one_day_duration

    day_checker(yesterday)
    day_checker(today)
    day_checker(tomorrow)
