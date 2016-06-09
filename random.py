#!/usr/bin/python

import libraries
import classes
from classes import Show

#create an array of show objects
def createObject(shows):
  show_array = []
  for show in shows.values():
    obj = classes.Show(show[0], show[2], show[3], show[1], show[4])
    show_array.append(obj)
  return show_array

def printShows(shows):
	for each in shows.values():
  	  print ("showname: {0} \n day: {1} \n begin_time: {2} \n end_time: {3} \n allTime_count: {4} \n" .format(each[0], each[1], each[2], each[3], each[4]))

#main program
if __name__ == "__main__":
 
  #try:
    # printShows(libraries.shows)
    shows = createObject(libraries.shows)
    print len(shows)
    for show in shows:
      print show.name
  #except: 
   # pass
