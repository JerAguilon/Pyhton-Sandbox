def decrement(hour, minute):
    minute -= 1
    if minute == -1:
        hour -= 1
        minute = 59
        if hour == -1:
            hour = 23
    print(format_time(hour, minute))
    return hour, minute

def is_valid(hour, minute, valid_digits):
    digits = [ int(hour / 10), hour % 10, int(minute / 10), minute % 10]
    return all([(i in valid_digits) for i in digits])

def format_time(hour, minute):
    hour = str(hour)
    minute = str(minute)
    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    return "{}:{}".format(hour, minute)

def solution(S):
    hour_and_minute = S.split(':')
    hour_and_minute = [int(i) for i in S.split(':')]
    hour = hour_and_minute[0]
    minute =  hour_and_minute[1]

    valid_digits = set([ int(hour / 10), hour % 10, int(minute / 10), minute % 10])
    while True:
        hour, minute = decrement(hour, minute)
        if is_valid(hour, minute, valid_digits):
            return format_time(hour, minute)

def test():
    print(solution("00:00"))
test()
