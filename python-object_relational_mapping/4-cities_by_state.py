#!/usr/bin/python3
"""script that lists all cities from the database"""
import MySQLdb
import sys

def list_cities(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = "SELECT * FROM cities ORDER BY id ASC"

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_cities(username, password, database)
