from datetime import datetime
from datetime import timedelta
from calendar import day_name

def add_time(*args):
    if len(args) == 2:
        info = '0001 01 01 {}'.format(args[0])

        start = datetime.strptime(info,'%Y %m %d %I:%M %p')
        stop = timedelta(hours   = int(args[1].split(':')[0]),
                         minutes = int(args[1].split(':')[1])) + start

        endDate = stop.strftime('%I:%M %p')
        if endDate[0] == '0': endDate = endDate[1:]
        difference = stop.day - start.day

        if difference == 0: return endDate
        elif difference == 1: return '{} (next day)'.format(endDate)
        else: return '{} ({} days later)'.format(endDate, difference)

    if len(args) == 3:
        day = list(day_name).index(args[2].title()) + 1
        info = '0001 01 0{} {}'.format(day, args[0])

        start = datetime.strptime(info,'%Y %m %d %I:%M %p')
        stop = timedelta(hours   = int(args[1].split(':')[0]),
                         minutes = int(args[1].split(':')[1])) + start

        endDate = stop.strftime('%I:%M %p')
        if endDate[0] == '0': endDate = endDate[1:]
        weekday = stop.strftime('%A')
        difference = stop.day - start.day

        if difference == 0: return '{}, {}'.format(endDate, weekday)
        elif difference == 1: return '{}, {} (next day)'.format(endDate, weekday)
        else: return '{}, {} ({} days later)'.format(endDate, weekday, difference)