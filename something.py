#!/usr/bin/python

import sys
from libraries import shows
import classes

USAGE = "tail -n [number of records or -f] access.log | python something.py"

# open database connection and retrieve values
db,cursor = classes.Show.connectDB()
classes.Show.createDB(db, cursor)
classes.Show.createShowsTable(db, cursor)
classes.Show.insertShows(db, cursor, shows)
dbShows = classes.Show.selectShows(db, cursor)
classes.Show.displayShows(dbShows)

'''
# create and print log_entry values
for logdata in sys.stdin.readlines():
  obj = classes.Log_entry(logdata)
  attrs = vars(obj)
  print '\n '.join("%s: %s" % item for item in attrs.items())
  print '\n'
'''
# update records
# classes.Show.insertShows(db, cursor, libraries.shows)

# close the connection
cursor.close()


