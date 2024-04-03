
'''pip install cx-Oracle
If you are using Python >= 3.6 use the below command in Windows: –

py -m pip install cx-Oracle
'''
import cx_Oracle

# Create a table in Oracle database
try:
 
    con = cx_Oracle.connect('capdd/next@localhost:1521/xe')
    print(con.version)
 
    # Now execute the sqlquery
    cursor = con.cursor()
 
    # Creating a table employee
    cursor.execute("create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")
 
    print("Table Created successfully")
 
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
 
# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()