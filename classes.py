import datetime
from time import strptime
import libraries
import MySQLdb as conn

__author__ = 'Christopher Jones'

################################################
# Shows: Stores data about shows on KRMA Radio #
################################################
class Show:
    def __init__(self, name, beginTime, endTime, dayofweek, counter):
        self.name = name
        self.beginTime = beginTime
        self.endTime = endTime
        self.dayofweek = dayofweek
        self.counter = counter
    

    ###############################################
    # connectDB: Establish connection to database #
    ###############################################
    @classmethod
    def connectDB(cls):
        db = conn.connect(host='localhost', user='krma', passwd='Bloodninja101010')
        cursor = db.cursor()
        return db, cursor
   
   
    ###################################################
    # createDB: Create new database if does not exist #
    ###################################################
    @classmethod
    def createDB(cls, db, cursor):
        # create a new database
        sql = '''
        DROP DATABASE IF EXISTS KRMA_Ratings;
        '''
        cursor.execute(sql)
        sql = '''
        CREATE DATABASE KRMA_Ratings;
        '''
        cursor.execute(sql)


    ################################################
    # createShowsTable: Establish values for shows #
    ################################################
    @classmethod
    def createShowsTable(cls, db, cursor):
        sql = 'USE KRMA_Ratings'
        cursor.execute(sql)
        #sql = 'DROP TABLE IF EXISTS shows;'
        #cursor.execute(sql)
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


    #################################################
    # selectShows: return all records from database #
    #################################################
    @classmethod
    def selectShows(cls, db, cursor):
        sql = 'select * from shows'
        cursor.execute(sql)
        # fetch all of the results
        dbShows = cursor.fetchall()
        return dbShows


    #########################################################
    # displayShows: Apparently dbShows is stored somewhere? #
    #########################################################
    @classmethod
    def displayShows(cls, dbShows):
        for each in dbShows:
          print each


    #########################################################
    # insertShows: Update the database with updated records #
    #########################################################
    @classmethod
    def insertShows(cls, db, cursor, shows):
        for each in shows.values():
          sql = "INSERT into shows(showname, day_begin, day_end, time_begin, time_end, allTime_count) values(%s, %s, %s, %s, %s, %s)"
          cursor.execute(sql, each)
        db.commit()


##################################################
# Log_entry: Records log entries from access.log #
##################################################
class Log_entry:
    def __init__(self, line):
        parts = self.parseData(line)
        self.ip = parts[0]
        self.user = parts[2]
        self.logDateTime = parts[3]
        self.time = self.whichHour(self.logDateTime)
        self.whatDay = self.exactDay(self.logDateTime)
        self.year = self.whatDay[0]
        self.month = self.whatDay[1]
        self.day = self.whatDay[2]
        self.dayofweek = self.dateToInt(self.year, self.month, self.day)
        self.http_method = parts[5]
        #self.host = host
        #self.page = page
        self.response_code = parts[8]
        #self.http_referer = http_referer
        #self.user_agent = user_agent
        #self.length = length
        self.showName = self.whichShow(self.time, self.dayofweek)


    ######################################################
    # parseData: parse lines of log data passed to class #
    ######################################################
    def parseData(self, line):
        parts = line.split()
        return parts


    #############################################################
    # dateToInt: This function returns a log date as an integer #
    #############################################################
    def dateToInt(self, year, month, day):
        dayofweek = datetime.date(year, month, day).isoweekday()
        return dayofweek


    #################################################################
    # whichHour: This function finds the hour the log was generated #
    #################################################################
    def whichHour(self, logDateTime):
        logTime = logDateTime[13:15] # the hour is within this index range
        return logTime # return the hour of the log generation


    ##############################################
    # exactDay: Return year month and day values #
    ##############################################
    def exactDay(self, logDateTime):
        yearStr = logDateTime[8:12]
        monthStr = logDateTime[4:7]
        dayStr = logDateTime[1:3]
        monthnum = strptime(monthStr, '%b').tm_mon
        year = int(yearStr)
        month = int(monthnum)
        day = int(dayStr)
        return year, month, day


    ##############################################################
    # whichShow: Use database entries in future for this process #
    ##############################################################
    def whichShow(self, strlogTime, strdayofweek):
        logTime = int(strlogTime)
        dayofweek = int(strdayofweek)
        if logTime in range(6, 9) and dayofweek in range(1, 5):
          return "Shannon Steele Show"
        elif(logTime in range(9, 12) and dayofweek in range(1, 5)):
          return "Herd-Will Geoff Show"
        elif(logTime in range(12, 15) and dayofweek in range(1, 5)):
          return "Vinnie's Midday Show"
        elif(logTime in range(15, 18) and dayofweek in range(1, 5)):
          return "Aleister and Maggie Show"
        elif(logTime in range(19, 23) and dayofweek == 3):
          return "Steve Jones Show"
        elif(logTime in range(19, 22) and dayofweek == 1):
          return "Eye on the Target Radio Show"
        elif(logTime in range(18, 23) and dayofweek == 2):
          return "Handy Randy Show"
        elif(logTime in range(18, 20) and dayofweek == 4):
          return "Brian 'Moonshine' Varner Show"
        elif(logTime in range(20, 23) and dayofweek == 4):
          return "Best Stams Sports Show"
        elif(logTime in range(18, 20) and dayofweek == 5):
          return "TJ Dylan Show"
        elif(logTime in range(20, 24) and dayofweek == 5):
          return "Some Kind of Radio Show"
        elif(logTime in range(10, 13) and dayofweek == 6):
          return "Frenemies News Radio Show"
        elif(logTime in range(15, 17) and dayofweek == 6):
          return "Zal & Zera Game Forum"
        elif(logTime in range(17, 19) and dayofweek == 6):
          return "Undaground Wrestling Show"
        elif(logTime in range(20, 24) and dayofweek == 6):
          return "Altered Realm Show"
        elif(logTime in range(14, 17) and dayofweek == 7):
          return "Bob Fritz Show"
        elif(logTime in range(19, 22) and dayofweek == 7):
          return "Sports to the Max Show"
        elif(logTime in range(22, 24) and dayofweek == 7):
          return "Laura Lyn's Psychic Power Show"
        else:
          return "undesignated time slot"
