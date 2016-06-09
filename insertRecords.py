#!/usr/bin/python
import libraries
import MySQLdb as conn

#################################################################################
# The plan for this program is to initialize the database with the library values
#################################################################################

def connectDB():
  db = conn.connect(host='localhost' ,user='krma', passwd='password', db='KRMA_Ratings')
  cursor = db.cursor()
  return db, cursor

def insertShows(db, cursor, shows):
  for each in shows.values():
    sql = "INSERT into shows(showname, day_begin, day_end, time_begin, time_end, allTime_count) values(%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, each)
  db.commit()
 
#main program
if __name__ == "__main__":
 
#  try:
    db, cursor = connectDB()
    insertShows(db, cursor, libraries.shows)
    #close the connection
    cursor.close()
#  except: 
#    pass
