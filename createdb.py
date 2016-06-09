#!/usr/bin/python
import MySQLdb

def connectDB():
    db = MySQLdb.connect(host='localhost', user='krma', passwd='password')
    cursor = db.cursor()
    return db, cursor

def createDB(db, cursor):
    # create a new database
    sql = '''
	DROP DATABASE IF EXISTS KRMA_Ratings;
        '''
    cursor.execute(sql)
    sql = ''' 
	CREATE DATABASE KRMA_Ratings;
	'''
    cursor.execute(sql)

def createShowsTable(db, cursor):
    sql = 'USE KRMA_Ratings'
    cursor.execute(sql)
    sql = 'DROP TABLE IF EXISTS shows;'
    cursor.execute(sql)
    sql = '''
	CREATE TABLE shows
	(showid int not null auto_increment,
	showname varchar(48) not null,
	day_begin int not null DEFAULT 0,
    day_end int not null DEFAULT 0,
	time_begin int not null DEFAULT 0,
	time_end int not null DEFAULT 0,
	current int not null DEFAULT 0,
	today_count int not null DEFAULT 0,
	week_count int not null DEFAULT 0,
	month_count int not null DEFAULT 0,
	year_count int not null DEFAULT 0,
	allTime_count int not null DEFAULT 0,
	primary key(showid))
	'''
    cursor.execute(sql)

#main program
if __name__ == "__main__":
    
    # exception handling routine   
    #try:
        db,cursor = connectDB()
        createDB(db, cursor)
        createShowsTable(db, cursor)
        #close the connection
        cursor.close()
    #except:
    #   pass
