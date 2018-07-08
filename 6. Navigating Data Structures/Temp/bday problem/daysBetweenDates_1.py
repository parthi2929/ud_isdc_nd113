def isLeapYear(year):
    """
    Check if an year is leap year or not
    Any year that is divisible by 400 is definitely a leap year.
    If it is not divisible by 400, then check if it is divisible by 100, if so, then it is NOT a leap year (even if it is divisible by 4), and
    If the above two conditions are not satisfied we check for divisibility by 4, it it is divisible by 4 it is a leap year.
    """
    if (year%400 ==0):
        return True
    elif (year%100 == 0):
        return False
    elif (year%4 ==0):
        return True
    else:
        return False
        

def daysInMonth(year, month):
    """
    Returns no of days in a month of an year
    Developmental steps:
    1. Return 30 always
    2. Return except taking leap year variation
    3. Include leap year variation
    """
    #return 30
    #assert (month >= 13),"Given month {} > 12".format(month)
    NoOfDaysArray = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year):
        NoOfDaysArray[1] = 29
    return NoOfDaysArray[month-1]

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!

    assert not dateIsBefore(year2, month2, day2,year1, month1, day1),"ERROR: End Date is before Start Date"
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed. Expected: ", answer, "  Result: ", result)
        else:
            print("Test case passed!")

test()