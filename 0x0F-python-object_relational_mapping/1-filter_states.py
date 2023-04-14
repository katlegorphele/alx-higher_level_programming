#!/usr/bin/python3


import sys
import MySQLdb

def main():
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

    # Execute SQL Query
    cursor.execute("SELECT * FROM states WHERE name LIKE '{letter}%' ORDER BY id ASC".format(letter='N'))

        # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close db connection
    db.close()

if __name__ == "__main__":
    main()
