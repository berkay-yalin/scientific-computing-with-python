WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def format_time(startTime, startDay=''):
    hour, minute = [int(i) for i in startTime.split(' ')[0].split(':')]
    day = 0

    if 'PM' in startTime:
        hour += 12
    if startDay != '':
        day = WEEKDAYS.index(startDay.capitalize())

    return {'d': day, 'H': hour, 'M': minute}

def add_time(startTime, duration, startDay = ''):
    start = format_time(startTime, startDay)
    diff = format_time(duration)
    stop = {
        'd': start['d'] + diff['d'],
        'H': start['H'] + diff['H'],
        'M': start['M'] + diff['M']
    }

    if stop['M'] > 60:
        stop['H'] += stop['M'] // 60
        stop['M'] = stop['M'] % 60
    if stop['H'] > 24:
        stop['d'] += stop['H'] // 24
        stop['H'] = stop['H'] % 24

    if stop['H'] > 12:
        output = f"{stop['H'] - 12}:{str(stop['M']).rjust(2, '0')} PM"
    elif stop['H'] == 12:
        output = f"12:{str(stop['M']).rjust(2, '0')} PM"
    elif stop['H'] == 0:
        output = f"12:{str(stop['M']).rjust(2, '0')} AM"
    else:
        output = f"{stop['H']}:{str(stop['M']).rjust(2, '0')} AM"

    if startDay != '':
        output += ', ' + str(WEEKDAYS[stop['d'] % 7])

    daydiff = stop['d'] - start['d']
    if daydiff == 1:
        output += ' (next day)'
    elif daydiff > 1:
        output += f' ({daydiff} days later)'

    return output
