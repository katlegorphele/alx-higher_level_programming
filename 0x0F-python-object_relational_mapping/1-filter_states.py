#!/usr/bin/python3
'''
script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
'''

import sys
import MySQLdb


if __name__ == '__main__':
   # Connect to DB
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL Query
    cursor.execute("SELECT * FROM states\
        WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close db connection
    db.close()
