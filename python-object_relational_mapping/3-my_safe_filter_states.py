#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states table"""
import MySQLdb
import sys

def search_state_safe(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        search_state_safe(username, password, database, state_name)
