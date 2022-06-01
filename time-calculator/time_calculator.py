from datetime import datetime
from datetime import datetime as dt
from datetime import timedelta
from calendar import day_name

def add_time(startHour, duration, startDay = None):
    def getStartTime(hour, day):
        return dt.strptime(f'0001 01 0{day} {hour}', '%Y %m %d %I:%M %p')

    def getStopTime(stopHour, stopMinute):
        return timedelta(hours = stopHour, minutes = stopMinute) + start

    def formatOutput(difference, endDate, weekday):
        if weekday == None:
            if difference == 0:
                return endDate
            elif difference == 1:
                return f'{endDate} (next day)'
            else:
                return f'{endDate} ({difference} days later)'
        else:
            if difference == 0:
                return f'{endDate}, {weekday}'
            elif difference == 1:
                return f'{endDate}, {weekday} (next day)'
            else:
                return f'{endDate}, {weekday} ({difference} days later)'

    ### PARENT FUNCTION ###
    if startDay == None:
        start = getStartTime(startHour, '1')
    else:
        start = getStartTime(startHour, list(day_name).index(startDay.title()) + 1)
    stop = getStopTime(*[int(i) for i in duration.split(':')])

    endDate = stop.strftime('%I:%M %p')
    if endDate[0] == '0':
        endDate = endDate[1:]

    if startDay == None:
        return formatOutput(stop.day - start.day, endDate, None)
    else:
        return formatOutput(stop.day - start.day, endDate, stop.strftime('%A'))
