"""
@author:  Zimon Kuhs.
@date:    2021-07-13.

Quick test script for checking that access to DBs is possible via Python connector.

TODO:     Remove when redundant?
"""

import os
import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  port = 3306,
  password = os.getenv("SQL_KEY"),
  db = "NUTRITION_DB"
)

queries = [
    "SELECT * FROM nutrition_choice"
]

results = []
cursor = mydb.cursor()

for query in queries:
    cursor.execute(query)
    results.append(cursor.fetchall())

for result in results:
    print(result)