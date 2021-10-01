# A script based on Microsoft's sample: https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python
# Note: Requires the creation of an Azure SQL Database: https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15&tabs=ssms

import argparse
import pyodbc
# The 'server', 'database', 'username', and 'password' variables need replacement.
server = '<server>.database.windows.net'
database = '<database>'
username = '<username>'
password = '<password>'   
driver= '{ODBC Driver 17 for SQL Server}'

abrv=[
    'AL',
    'AK',
    'AZ',
    'AR',
    'CA',
    'CO',
    'CT',
    'DE',
    'FL',
    'GA',
    'HI',
    'ID',
    'IL',
    'IN',
    'IA',
    'KS',
    'KY',
    'LA',
    'ME',
    'MT',
    'NE',
    'NV',
    'NH',
    'NJ',
    'NM',
    'NY',
    'NC',
    'ND',
    'OH',
    'OK',
    'OR',
    'MD',
    'MA',
    'MI',
    'MN',
    'MS',
    'MO',
    'PA',
    'RI',
    'SC',
    'SD',
    'TN',
    'TX',
    'UT',
    'VT',
    'VA',
    'WA',
    'WV',
    'WI',
    'WY',
    ]
states={
    'AL' : 'Alabama',
    'AK' : 'Alaska',
    'AZ' : 'Arizona',
    'AR' : 'Arkansas',
    'CA' : 'California',
    'CO' : 'Colorado',
    'CT' : 'Connecticut',
    'DE' : 'Delaware',
    'FL' : 'Florida',
    'GA' : 'Georgia',
    'HI' : 'Hawaii',
    'ID' : 'Idaho',
    'IL' : 'Illinois',
    'IN' : 'Indiana',
    'IA' : 'Iowa',
    'KS' : 'Kansas',
    'KY' : 'Kentucky',
    'LA' : 'Louisiana',
    'ME' : 'Maine',
    'MT' : 'Montana',
    'NE' : 'Nebraska',
    'NV' : 'Nevada',
    'NH' : 'New Hampshire',
    'NJ' : 'New Jersey',
    'NM' : 'New Mexico',
    'NY' : 'New York',
    'NC' : 'North Carolina',
    'ND' : 'North Dakota',
    'OH' : 'Ohio',
    'OK' : 'Oklahoma',
    'OR' : 'Oregon',
    'MD' : 'Maryland',
    'MA' : 'Massachusetts',
    'MI' : 'Michigan',
    'MN' : 'Minnesota',
    'MS' : 'Mississippi',
    'MO' : 'Missouri',
    'PA' : 'Pennsylvania',
    'RI' : 'Rhode Island',
    'SC' : 'South Carolina',
    'SD' : 'South Dakota',
    'TN' : 'Tennessee',
    'TX' : 'Texas',
    'UT' : 'Utah',
    'VT' : 'Vermont',
    'VA' : 'Virginia',
    'WA' : 'Washington',
    'WV' : 'West Virginia',
    'WI' : 'Wisconsin',
    'WY' : 'Wyoming'
    }

# class Str is used to process arguments as state abbreviations; these
# are then used as a mapping to the full name.
class Str :
    pass
s = Str()

# The parser used to process the command line arguments.
parser = argparse.ArgumentParser(
    description='A script returning products sold based on the state in which the sale took place.')
parser.add_argument(
    '--st', choices=abrv,
    help='An example: To see sales made in Alabama use \'python salebystate.py --st AL\'')
args = parser.parse_args(namespace=Str)

# The script connecting to the 'Adventure Works' database (see 'README.md' for more information).
with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("CREATE SCHEMA Abbreviations")
        conn.commit()
        cursor.execute("CREATE TABLE Abbreviations.StateProvince ( Name VARCHAR(255) NOT NULL, Abbreviation VARCHAR(255) NOT NULL )")
        conn.commit()
        cursor.execute("INSERT INTO Abbreviations.StateProvince (Name, Abbreviation) VALUES ( N'Alaska', N'AL')")
        conn.commit()
        cursor.execute("SELECT TOP 10 a.Name, a.Abbreviation FROM Abbreviations.StateProvince as a ORDER BY a.Name ASC;")
        row = cursor.fetchone()
        print("State\t\t\tAbbreviation")
        while row:
            print(str(row[0]) + '\t\t\t' + str(row[1]))
            row = cursor.fetchone()
