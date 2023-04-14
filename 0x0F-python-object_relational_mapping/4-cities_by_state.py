#!/usr/bin/env python3

#script that lists all cities from the database hbtn_0e_4_usa
import sys
import MySQLdb

if __name__ == '__main__':

    #Get command line args
    u_name = sys.argv[1]
    sql_pass = sys.argv[2]
    sql_db = sys.argv[3]

    #Connect to DB
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user = u_name,
        passwd=sql_pass,
        db = sql_db
    )

    # Create cursor object
    cursor = db.cursor()

    #construct SQL Query
    sql_query = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    # Execute SQL Query
    cursor.execute(sql_query)

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close db connection
    db.close()
    
