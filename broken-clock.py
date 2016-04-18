import datetime


def convert_error(time, unit):
    multi = {'h': 3600, 'm': 60, 's': 1}
    return int(time) * multi[unit[0]]


def calculate_error(error_description):
    error, unit, _, time, t_unit = error_description.split()
    error = convert_error(error, unit)
    time = convert_error(time, t_unit)
    return error/time


def broken_clock(starting_time, wrong_time, error_description):
    start = datetime.datetime.strptime(starting_time, '%H:%M:%S')
    wrong_end = datetime.datetime.strptime(wrong_time, '%H:%M:%S')

    error = calculate_error(error_description)

    wrong_delta = (wrong_end - start).total_seconds()
    delta = datetime.timedelta(seconds=(wrong_delta / (1 + error)))

    return (start + delta).strftime('%H:%M:%S')


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
