#!/usr/bin/python3
"""
Script that lists all states from the database
hbtn_0e_0_usa starting with N
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    req = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(req)

    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
