#!/usr/bin/python

import MySQLdb as conn
import libraries

def connectDB():
  db = conn.connect(host='localhost', user='krma', passwd='password', db='KRMA_Ratings')
  cursor = db.cursor()
  return db, cursor

def selectShows(db, cursor):
  sql = 'select * from shows'
  cursor.execute(sql)
  # fetch all of the results
  dbShows = cursor.fetchall()
  return dbShows

def displayShows(dbShows):
  for each in dbShows:
    print each
  
#main program
if __name__ == "__main__":

# exception handling routine   
  try:
    db, cursor = connectDB()
    dbShows = selectShows(db, cursor)
    cursor.close()
    displayShows(dbShows)
  except: 
    pass
