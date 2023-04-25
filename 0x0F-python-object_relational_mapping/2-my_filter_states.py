#!/usr/bin/python3
"""
    This script takes in an
    argument and displays all
    values in the states table
    of hbtn_0e_0_usa where name
    matches the argument.
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    try:
        db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3]
        )
    except Exception:
        print("Can't connect to database")
        exit(1)

    searched_state = argv[4]

    # Create cursor object
    cursor = db.cursor()

    # Execute SQL Query
    cursor.execute(
        "SELECT * \
                   FROM states \
                   WHERE name = '{state}' \
                   ORDER BY id ASC".format(
            searched_state
        )
    )

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close db connection
    db.close()
