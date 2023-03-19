#!/usr/bin/python3
'''Takes in an argument and lists filtered data from
a table in a database that matches the argument'''

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id \
    WHERE (states.name = '{}') \
    ORDER BY states.id".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in range(len(rows)):
        print("".format(cur.fetchone()), end=", ")

    # length = len(rows)
    # for row in rows:
    #     for col in row:
    #         length -= 1
    #         print(col, end="")
    #         if (length != 0):
    #             print(", ", end="")
    #         else:
    #             print()
    cur.close()
    db.close()
