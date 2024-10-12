import pandas as pd
import mysql.connector
import numpy as np

# MySQL database connection setup
conn = mysql.connector.connect(
    host="localhost",
    user="sqluser",      # MySQL username
    password="901741",  # MySQL password
    database="start_project"   # Name of your database
)

cursor = conn.cursor()

# Read the CSV file
data = pd.read_csv('C:/Users/jidax/OneDrive/Desktop/Personal Project/Data Prep/Impact_of_Remote_Work_on_Mental_Health.csv')  # Replace with your CSV file path

# Replace NaN values with the string 'None'
data.fillna('None', inplace=True)

# Optional: Strip whitespace from all string values in the DataFrame
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Check the shape of the DataFrame
print(f"DataFrame shape: {data.shape}")
print("Column names:")
print(data.columns.tolist())

# Debugging: Print the first few rows of the DataFrame to inspect data
print("Data from CSV (first few rows):")
print(data.head())  # Show the first few rows of the DataFrame

# Prepare to collect values for insertion
values = []

# Insert data into the single table
for index, row in data.iterrows():
    row_values = []
    for value in row:
        # Keep the string 'None' if that's how we set it
        row_values.append(value)
    values.append(tuple(row_values))

# Debugging: Check lengths of each row values
for i, value_tuple in enumerate(values):
    print(f"Row {i}: {value_tuple} (Length: {len(value_tuple)})")  # Print each row and its length

# Prepare SQL query for insertion (without Motivation_Level)
sql = """
INSERT INTO data_collected (
    Employee_ID,
    Age,
    Gender,
    Job_Role,
    Industry,
    Years_of_Experience,
    Work_Location,
    Hours_Worked_Per_Week,
    Number_of_Virtual_Meetings,
    Work_Life_Balance_Rating,
    Stress_Level,
    Mental_Health_Condition,
    Access_to_Mental_Health_Resources,
    Productivity_Change,
    Social_Isolation_Rating,
    Satisfaction_with_Remote_Work,
    Company_Support_for_Remote_Work,
    Physical_Activity,
    Sleep_Quality,
    Region
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Execute the insertion for each row
for value_tuple in values:
    if len(value_tuple) != 20:  # Check if the length matches 20 now
        print(f"Skipping row due to length mismatch: {value_tuple} (Length: {len(value_tuple)})")
        continue  # Skip this iteration if lengths don't match
    try:
        cursor.execute(sql, value_tuple)
    except mysql.connector.Error as err:
        print(f"Error inserting row {value_tuple}: {err}")  # Print error message if insertion fails

# Commit the transaction and close the connection
conn.commit()
cursor.close()
conn.close()

print("Data insertion process completed.")