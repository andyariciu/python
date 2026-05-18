import os
import pypyodbc as odbc
import pandas as pd
import json

def load_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Database connection
config = load_config('appsettings.json')
DRIVER_NAME = config['ConnectionSettings']['DatabaseSettings']['DRIVER_NAME']
SERVER_NAME =  config['ConnectionSettings']['DatabaseSettings']['SERVER_NAME']
DATABASE_NAME = config['ConnectionSettings']['DatabaseSettings']['DATABASE_NAME']

# uid=<username>;
# pwd=<password>;
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

""""
# Execute a query
cursor.execute("SELECT * FROM Notifications")

# Fetch the results
results = cursor.fetchall()

# Iterate over the results and print each row
for row in results:    print(row)

# Close the cursor and connection
cursor.close()
"""
column_names=["ID","Cell",'Status', 'Message', 'Created', 'Last update', 'Issue type', 'Inspector ID', 'Created by', 'Modified by', 'Urgency Level', 'Department', 'Postponed at', 'Checked at', 'Solved at','ResMsg', 'Days to solve']
home_directory = os.path.expanduser("~")
# Construct the path to the Desktop
desktop_directory = os.path.join(home_directory, "Desktop")
# Define the new directory name
new_directory_name = "Downtime Measurement Data"
directory = os.path.join(desktop_directory, new_directory_name)

df = pd.read_sql_query('SELECT * FROM Notifications', conn)

if not os.path.exists(directory):
    os.makedirs(directory)

df['Days to solve'] = df['solvedat'] - df['datetime']
df.columns = column_names
df.to_excel(os.path.join(directory, 'ExportedData.xlsx'), index=False)
conn.close()