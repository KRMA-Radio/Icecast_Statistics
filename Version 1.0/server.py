#!/usr/bin/python

__author__ = 'Chris'

import string # Check if this module is needed / being used
import sys
import time # Check if this module is needed / being used
import datetime
from time import strptime

global showCounters
showCounters = {
  'counter0' : 0,
  'counter1' : 0,
  'counter2' : 0,
  'counter3' : 0,
  'counter4' : 0,
  'counter5' : 0,
  'counter6' : 0,
  'counter7' : 0,
  'counter8' : 0,
  'counter9' : 0,
  'counter10' : 0,
  'counter11' : 0,
  'counter12' : 0,
  'counter13' : 0,
  'counter14' : 0,
  'counter15' : 0,
  'counter16' : 0,
  'counter17' : 0,
  'counter18' : 0
  }

################################################################
# List of show names 
# Create a library with corresponding time slots?
# can you include two ranges in a library? Test it.
# Create an object with properties?
################################################################

global slots
slots = [
  "the Shannon Steele Show",
  "the Herd-Will Geoff Show",
  "the Vinnie's Midday Show",
  "the Aleister and Maggie Show",
  "the Steve Jones Show",
  "the Eye on the Target Radio Show",
  "the Handy Randy Show",
  "the Brian 'Moonshine' Varner Show",
  "the Best Stams Sports Show",
  "the TJ Dylan Show",
  "Some Kind of Radio Show",
  "the Frenemies News Radio Show",
  "the Zal & Zera Game Forum",
  "the Undaground Wrestling Show",
  "the Altered Realm Show",
  "the Bob Fritz Show",
  "the Sports to the Max Show",
  "Laura Lyn's Psychic Power Show",
  "an undesignated time slot"
  ]

################################################################
# Create list of show times / range to programatically sort logs
################################################################

#########################################################
# Create function to distiguish unique IP's for listeners
#########################################################

#######################################################################################
# I hard coded the show names and corresponding slots for clarity in their relationship
# An interface or section of code might later be created for faster edits
#######################################################################################

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
  elif(logTime in range(15,23) and dayofweek == 3):
#   print "This is the Steve Jones Show"
    showCounters['counter4'] += 1
  elif(logTime in range(15,22) and dayofweek == 1): #There is overlap with Aleister & Maggie
#   print "This is the Eye on the Target Radio Show"
    showCounters['counter5'] += 1
  elif(logTime in range(18,23) and dayofweek == 2): #Double check these...
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

##############################
# Create log output to console
##############################

def outputToConsole(): 
  for i in range(len(slots)):
    print "Total number of listeners for", slots[i]+ ':', showCounters['counter'+str(i)], '\n' 

################################################
# This function returns a log date as an integer
################################################
def dateToInt(year, month, day):
  dayofweek = datetime.date(year, month, day).isoweekday()
  return dayofweek

####################################################
# This function finds the hour the log was generated
####################################################
def whichHour(logDateTime):  
#  for data in logdata:
#    s = data.split() # turn log entries into individual indices
#    logDateTime = s[3] # the third index is the datetime
    logTime = logDateTime[13:15] # the hour is within this index range
    return logTime # return the hour of the log generation

##################################
# Return year month and day values 
##################################
def exactDay(logDateTime):
#  for data in logdata:
#    s = data.split() # return log entries as indices
#    logDateTime = s[3] # The third index is the datetime
    yearstr = logDateTime[8:12]
    monthStr = logDateTime[4:7] 
    daystr = logDateTime[1:3]
    monthnum = strptime(monthStr,'%b').tm_mon
    year = int(yearstr)
    month = int(monthnum)
    day = int(daystr)
    return year, month, day # return list with these values? or just return them?

################
# main program #
################
if __name__ == "__main__":

  try:
    data = sys.stdin.readlines() 
    for sl in data: # My goal for this loop is to keep a count of each show in log
      s = sl.split()
      logDateTime = s[3]
#      print logDateTime
      logTime = whichHour(logDateTime)
#      print logTime
      year, month, day = exactDay(logDateTime)
#      print year, month, day
      dayofweek = dateToInt(year, month, day)
#      print dayofweek
      whichShow(logTime, dayofweek)
    outputToConsole()
   
  except:
    pass
