#!/usr/bin/python3
'''
script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
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
        db=sys.argv[3]
    )

    # Create cursor object
    cursor = db.cursor()

    # Construct SQL Query
    sql_query = "SELECT * \
                FROM states \
                WHERE name = '{state}' \
                ORDER BY id ASC".format(state=sys.argv[4])

    # Execute SQL Query
    cursor.execute(sql_query)

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close db connection
    db.close()
