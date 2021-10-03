# A script based on Microsoft's sample: https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python
# Note: Requires the creation of an Azure SQL Database: https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15&tabs=ssms
import pyodbc
from definitions import connection_string, states, Print

# Database schema and table creation strings.
schema = 'Abbreviations'
table = 'StateProvince'
col_1 = 'Name'
col_2 = 'Abbreviation'

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
                            """, states)

        cursor.execute(f"""
                        SELECT a.{col_1}, a.{col_2} 
                        FROM {schema}.{table} as a 
                        ORDER BY a.{col_1} ASC;
                        """)
        rows = cursor.fetchall()

        Print(col_1, col_2)
        for row in rows:
            Print(row.Name, row.Abbreviation)
