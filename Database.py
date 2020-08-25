import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        try:
            self.__conn = sqlite3.connect("pkbattlestraining.db")
            self.__cursor = self.__conn.cursor()
        except Error as e:
            print(e)
    # 1
    def getDatas(self):
        try:
            self.__cursor.execute("SELECT * from historialnumber")
            return self.__cursor.fetchall()
        except Error as e:
            print(e)
    # 2
    def insertDatas( self, datas):
        try:
            for row in datas:
                self.__cursor.execute("INSERT INTO historialnumber VALUES(?,?,?,?,?,?,?,?,?)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
            
            self.__conn.commit()
        except Error as e:
            print(e)