import sqlite3
#import of sqlite module
#from the module import Error
from sqlite3 import Error



##############################################################################################################

def sql_connection():
    try:
        con = sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)") #creating a table
    cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')") #adding new values
    con.commit()

con = sql_connection()
#sql_table(con)

##############################################################################################################
def sql_insert(con, entities):
    
    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    
    con.commit()

entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

sql_insert(con, entities)
##############################################################################################################

def sql_update(con):
    
    cursorObj = con.cursor()

    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')

    con.commit()

sql_update(con)

##############################################################################################################
def sql_fetch(con):
    
    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM employees')
    #cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(con)
#[print(row) for row in cursorObj.fetchall()]
##############################################################################################################




