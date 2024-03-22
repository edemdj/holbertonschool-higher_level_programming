#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""
import MySQLdb
import sys

def list_states_with_N_starting(username, password, database):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
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
        list_states_with_N_starting(username, password, database)
