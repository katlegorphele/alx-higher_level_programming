#!/usr/bin/python3
"""
SQL Injection safe script
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql
    import re

    if (len(argv) != 5):
        print('Use: username, password, db name, state name')
        exit(1)

    searched = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('Enter a valid state name')
        exit(1)

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Can\'t connect to database')
        exit(1)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name = '{:s}' ORDER BY id ASC;".format(searched))

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()