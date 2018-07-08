# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
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
    return [nextYear, nextMonth, nextDay]

def isBefore(dateCurrent, dateFinal):
    """
    Returns true if dateCurrent is before dateFinal else false
    """
    currentDay = dateCurrent[2]
    currentMonth = dateCurrent[1]
    currentYear = dateCurrent[0]
    finalDay = dateFinal[2]
    finalMonth = dateFinal[1]
    finalYear = dateFinal[0]
    if (currentYear < finalYear):
        return True
    elif (currentYear == finalYear):
        if (currentMonth < finalMonth):
            return True
        elif (currentMonth == finalMonth):
            if (currentDay < finalDay):
                return True
            else:
                return False
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    assert not isBefore([year2, month2, day2],[year1, month1, day1]),"ERROR: End Date is before Start Date"
    days = 0
    dateCurrent = [year1, month1, day1]
    dateFinal = [year2, month2, day2]
    while ( isBefore(dateCurrent, dateFinal) ):
        dateCurrent = nextDay(dateCurrent[0], dateCurrent[1], dateCurrent[2])
        #print(days)
        days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()
# print('Next day is: {}'.format(nextDay([1999, 12, 30])))
# print('Next day is: {}'.format(nextDay([2013, 1, 30])))
# print('Next day is: {}'.format(nextDay([2012, 12, 30])))
    
