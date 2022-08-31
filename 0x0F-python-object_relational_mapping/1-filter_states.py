#!/usr/bin/python3
"""script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


def states_startn():
    """Takes 3 arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name"""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()


if __name__ == "__main__":
    states_startn()
