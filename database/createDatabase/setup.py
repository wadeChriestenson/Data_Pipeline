# install dependencies
import pandas as pd
import sqlite3


# Read CSV and get column names
def read_column_names():
    df = pd.read_csv('http://www.census.gov/programs-surveys/cbp/data/datasets.html County Business Patterns survey results, 1986-2014, CSV')
    column_names = df.columns

    # Generate column definitions
    column_definitions = ', '.join([f'{col} TEXT' for col in column_names])
    # final_col_definitions = column_definitions.replace("VIN 1-10 TEXT", "VIN INTEGER PRIMARY KEY")
    return column_definitions


def create_table_vehicles(name_of_columns):
    # Create SQLite database and table
    con = sqlite3.connect('../db/master.sqlite')
    cur = con.cursor()

    # Create the table query dynamically
    create_table_query = f'CREATE TABLE IF NOT EXISTS main.mainData ({name_of_columns})'

    # Execute the CREATE TABLE query
    cur.execute(create_table_query)

    # Commit the changes and close the connection
    con.commit()
    con.close()


def populate_mainData_table():
    df = pd.read_csv('http://www.census.gov/programs-surveys/cbp/data/datasets.html County Business Patterns survey results, 1986-2014, CSV')
    con = sqlite3.connect('../db/master.sqlite')

    # Insert data into the table
    df.to_sql('mainData', con, if_exists='replace', index=False)

    # Commit the changes and close the connection
    con.commit()
    con.close()


column = read_column_names()
# print(column)
create_table_vehicles(column)
populate_mainData_table()
