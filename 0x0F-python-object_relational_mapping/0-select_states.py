#!/usr/bin/python3
'''
Lists all states from hbtn_0e_0_usa database
'''

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to MySQL server running on localhost port 3306
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)

    # Create cursor object
    cur = db.cursor()

    # Execute SQL Query
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    # Fetch all rows and return as list of tuples
    rows = cur.fetchall()

    # Print each row of result set
    for row in rows:
        print(row)

    # Close cursor object and MySQL connection
    cur.close()
    db.close()
