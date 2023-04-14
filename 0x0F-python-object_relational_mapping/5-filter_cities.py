#!/usr/bin/python3

# script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

import sys
import MySQLdb

if __name__ == '__main__':
    # Get command line args
    u_name = sys.argv[1]
    sql_pass = sys.argv[2]
    sql_db = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to DB
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=u_name,
        passwd=sql_pass,
        db=sql_db
    )

    # Create cursor object
    cursor = db.cursor()

    # construct SQL Query
    sql_query = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = '{state}' ORDER BY cities.id ASC".format(state=state_name)

    # Execute SQL Query
    cursor.execute(sql_query)

    # Fetch all rows and print them
    rows = cursor.fetchall()
    # extract the city names from the rows
    cities = [row[0] for row in rows]
    # print the cities, separated by commas
    print(', '.join(cities))
    
    # Close db connection
    db.close()
