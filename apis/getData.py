# install dependencies
import sqlite3


def get_table():
  # Create SQLite database and table
  con = sqlite3.connect('../database/db/vehicles.sqlite')
  cur = con.cursor()

  # Execute the SELECT query
  cur.execute("SELECT * "
              "FROM mainData "
              "WHERE State='BC'"
              )

  cur.execute("DELETE FROM mainData "
              "WHERE State = 'BC'")
  cur.execute("DELETE FROM mainData "
              "WHERE State = 'State'")


  # Fetch all rows from the result
  allData = cur.fetchall()

  # Close the connection
  con.close()

  return allData


table_data = get_table()
print(table_data)
