#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities"""
import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s ORDER BY cities.id ASC"

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
        list_cities_by_state(username, password, database, state_name)
