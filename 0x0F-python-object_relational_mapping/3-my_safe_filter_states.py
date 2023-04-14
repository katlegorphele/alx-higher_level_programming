#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    
    #Get command line args
    u_name = sys.argv[1]
    sql_pass = sys.argv[2]
    sql_db = sys.argv[3]
    state_name = sys.argv[4]

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

    #Construct SQL Query
    sql_query = "SELECT * FROM states WHERE name = '{state}' ORDER BY id ASC".format(state=state_name)

    # Execute SQL Query
    cursor.execute(sql_query)

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close db connection
    db.close()
