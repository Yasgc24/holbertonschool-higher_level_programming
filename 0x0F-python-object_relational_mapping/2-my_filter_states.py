#!/usr/bin/python3
"""takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
from sys import argv


def state():
    """Takes 4 arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: state name
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                ORDER BY id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()


if __name__ == "__main__":
    state()
