###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    This version assumes all months have 30 days
    """
    # YOUR CODE HERE
    nextDay = day
    nextMonth = month
    nextYear = year
    if (day < 30):
        nextDay += 1
    if (day == 30):
        nextDay = 1
        if (month < 12):
            nextMonth += 1
        if (month == 12):
            nextMonth = 1
            nextYear += 1
    return (nextYear, nextMonth, nextDay)

print('Next day is: {}'.format(nextDay(1999, 12, 30)))
print('Next day is: {}'.format(nextDay(2013, 1, 30)))
print('Next day is: {}'.format(nextDay(2012, 12, 30)))