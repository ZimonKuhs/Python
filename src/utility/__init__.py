import calendar
import time

LIMIT = 10

def secondsToDayTime(epochSeconds) :
    days, seconds = divmod(epochSeconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    return [days, hours, minutes, seconds]

if __name__ == "__main__" :
    today = secondsToDayTime(calendar.timegm(0) - int(time.time()))
    print("%d - %d:%d:%d" % (today[0], today[1], today[2], today[3]))
