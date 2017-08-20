from datetime import date
import calendar

class MeetupDayException(Exception):
  pass

def meetup_day(year, month, weekday, prop):
  dates = [date(year, month, day) for day, wday in calendar.Calendar().itermonthdays2(year, month) if day and wday == getattr(calendar, weekday.upper())]

  if prop == 'teenth':
    return dates[1] if dates[1].day in range(13, 20) else dates[2] # teenth day is in either the second or the third week
  elif prop[0].isdigit():
    if int(prop[0]) > len(dates): raise MeetupDayException
    return dates[int(prop[0]) - 1]
  elif prop == 'last':
    return dates[-1]
  else:
    raise ValueError
