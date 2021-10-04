"""
A script based on Microsoft's 2019 version of the 'AdventureWorks' (OLTP) sample database:
          https://github.com/Microsoft/sql-server-samples/releases/tag/adventureworks
Note: The previously used light-weight version, 'AdventureWorksLT,' was swapped in favor of the complete version.
"""
import argparse
import pyodbc
from definitions import connection_string, states, Print

# Database schema and table creation strings.
schema = 'Abbreviations'
table = 'StateProvince'
col_1 = 'Name'
col_2 = 'Abbreviation'

# class Str is used to process arguments as state abbreviations; these
# are then used as a mapping to the full name.
class Str :
    pass
s = Str()

# The parser used to process the command line arguments.
parser = argparse.ArgumentParser(
    description='A script returning products sold based on the state in which the sale took place.')
parser.add_argument(
    '--st', choices=states.keys(),
    help='An example: To see sales made in Alabama use \'python salebystate.py --st AL\'')
args = parser.parse_args(namespace=Str)

# The script connecting to the 'Adventure Works' database (see 'README.md' for more information).
with pyodbc.connect(connection_string) as conn:
    with conn.cursor() as cursor:
        # Debugging.
        cursor.execute(f"""
                        DROP TABLE IF EXISTS {schema}.{table};
                        DROP SCHEMA IF EXISTS {schema};
                        """)
        # Add abbreviations for ease of future access.
        cursor.execute(f"CREATE SCHEMA {schema};")
        cursor.execute(f"""
                        CREATE TABLE {schema}.{table}
                        ({col_1} VARCHAR(255) NOT NULL,
                        {col_2} VARCHAR(255) NOT NULL);
                        """)
        # Add values in states into cursor before sending them to the server.
        cursor.executemany(f"""
                            INSERT INTO {schema}.{table} ({col_1}, {col_2})
                            VALUES (?, ?)
                            """, [(abb, states[abb]) for abb in states.keys()])

        cursor.execute(f"""
                        SELECT a.{col_1}, a.{col_2} 
                        FROM {schema}.{table} as a 
                        ORDER BY a.{col_1} ASC;
                        """)

        cursor.execute(f"""
                        SELECT DISTINCT ps.{col_1}, p.{col_1} 
                        FROM Production.Product p, Sales.SalesOrderDetail od, Sales.SalesOrderHeader oh, Sales.Customer ca, Person.{table} ps
                        WHERE p.ProductID = od.ProductID 
                        AND od.SalesOrderID = oh.SalesOrderID 
                        AND oh.CustomerID = ca.CustomerID 
                        AND ca.TerritoryID = ps.TerritoryID 
                        AND ps.{col_1} = '{states[s.st]}' 
                        ORDER BY ps.{col_1} ASC;
                        """)

        rows = cursor.fetchall()
        Print(col_1, col_2)
        for row in rows:
            Print(row[0], row[1])
