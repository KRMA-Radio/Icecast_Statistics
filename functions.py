from time import strptime
import datetime

#############################################################
# dateToInt: This function returns a log date as an integer #
#############################################################
def dateToInt(year, month, day):
    dayofweek = datetime.date(year, month, day).isoweekday()
    return dayofweek

#################################################################
# whichHour: This function finds the hour the log was generated #
#################################################################
def whichHour(logDateTime):
    logTime = logDateTime[13:15] # the hour is within this index range
    return logTime # return the hour of the log generation

##############################################
# exactDay: Return year month and day values #
##############################################
def exactDay(logDateTime):
    yearStr = logDateTime[8:12]
    monthStr = logDateTime[4:7]
    dayStr = logDateTime[1:3]
    monthnum = strptime(monthStr,'%b').tm_mon
    year = int(yearStr)
    month = int(monthnum)
    day = int(dayStr)
    return year, month, day

####################################################################################################
# whichShow: I hard coded the show names and corresponding slots for clarity in their relationship #
####################################################################################################

def whichShow(strlogTime, strdayofweek):
    logTime = int(strlogTime)
    dayofweek = int(strdayofweek)
    if logTime in range(6,9) and dayofweek in range(1,5):
    #   print "This is the Shannon Steele Show" # Will pass in function
      showCounters['counter0'] += 1
    elif(logTime in range(9,12) and dayofweek in range(1,5)):
    #   print "This is the Herd-Will Geoff Show"
      showCounters['counter1'] += 1
    elif(logTime in range(12,15) and dayofweek in range(1,5)):
    #   print "This is Vinnie's Midday Show"
      showCounters['counter2'] += 1
    elif(logTime in range(15,18) and dayofweek in range(1,5)):
    #   print "This is the Aleister and Maggie Show"
      showCounters['counter3'] += 1
    elif(logTime in range(19,23) and dayofweek == 3):
    #   print "This is the Steve Jones Show"
      showCounters['counter4'] += 1
    elif(logTime in range(19,22) and dayofweek == 1):
    #   print "This is the Eye on the Target Radio Show"
      showCounters['counter5'] += 1
    elif(logTime in range(18,23) and dayofweek == 2):
    #   print "This is the Handy Randy Show"
      showCounters['counter6'] += 1
    elif(logTime in range(18,20) and dayofweek == 4):
    #   print "This is the Brian 'Moonshine' Varner Show"
      showCounters['counter7'] += 1
    elif(logTime in range(20,23) and dayofweek == 4):
    #   print "This is the Best Stams Sports Show"
      showCounters['counter8'] += 1
    elif(logTime in range(18,20) and dayofweek == 5):
    #   print "This is the TJ Dylan Show"
      showCounters['counter9'] += 1
    elif(logTime in range(20,24) and dayofweek == 5): #this one might break (no 24th hour)
    #   print "This is Some Kind of Radio Show"
      showCounters['counter10'] += 1
    elif(logTime in range(10,13) and dayofweek == 6):
    #   print "This is the Frenemies News Radio Show"
      showCounters['counter11'] += 1
    elif(logTime in range(15,17) and dayofweek == 6):
    #   print "This is the Zal & Zera Game Forum"
      showCounters['counter12'] += 1
    elif(logTime in range(17,19) and dayofweek == 6):
    #   print "This is the Undaground Wrestling Show"
      showCounters['counter13'] += 1
    elif(logTime in range(20,24) and dayofweek == 6): #another one with same issue
    #   print "This is the Altered Realm Show"
      showCounters['counter14'] += 1
    elif(logTime in range(14,17) and dayofweek == 7):
    #   print "This is the Bob Fritz Show"
      showCounters['counter15'] += 1
    elif(logTime in range(19,22) and dayofweek == 7):
    #   print "This is the Sports to the Max Show"
      showCounters['counter16'] += 1
    elif(logTime in range(22,24) and dayofweek == 7):
    #   print "This is Laura Lyn's Psychic Power Show"
      showCounters['counter17'] += 1
    else:
    #   print "This is an undesignated time slot"
      showCounters['counter18'] += 1