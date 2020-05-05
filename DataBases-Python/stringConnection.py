import MySQLdb
import mysql.connector

def getAllRows():
    try:
        connection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Franco2!2!",  # your password
                     db="HARMOND_DBA")        # name of the data base

        cursor = connection.cursor()
        print("Connected to MySQL")

        MySQL_select_query = """SELECT * from Employee"""
        cursor.execute(MySQL_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        """print("Printing each row")
        for row in records:
            print("HarmonID: ", row[6])
            print("Full Name: ", row[4])
            print("Start Day: ", row[5])
            print("Picture: ", row[7])
            print("\n")"""

        cursor.close()
    except MySQLdb.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The MySQL connection is closed")

getAllRows()


def insertRow():
    try:
        connection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Franco2!2!",  # your password
                     db="HARMOND_DBA")        # name of the data base

        cursor = connection.cursor()
        print("Connected to MySQL")

        sql = """INSERT INTO employee VALUES
        (   id,
            'Adrian', 
            'Badilla', 
            'Chinchilla', 
             NULL, 
             timestamp('2020-02-08'), 
             'AB80',  
             NULL);""" 

        cursor.execute(sql)
        connection.autocommit(True)
        cursor.close()

        print("executed "+sql)

    except MySQLdb.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The MySQL connection is closed")

def insertValues():
    try:
        connection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Franco2!2!",  # your password
                     db="HARMOND_DBA")        # name of the data base

        cursor = connection.cursor()
        print("Connected to MySQL")

        sql ="""INSERT INTO employee VALUES
        (   id,
            'Adrian', 
            'Badilla', 
            'Chinchilla', 
             NULL, 
             timestamp('2020-02-08'), 
             'AB80',  
             NULL);"""

        cursor.execute(sql)

        cursor.commit()

        print(cursor.rowcount, "record inserted.")

    except MySQLdb.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The MySQL connection is closed")



insertRow()
getAllRows()
