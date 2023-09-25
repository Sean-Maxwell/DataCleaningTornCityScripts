#Rename f = pd.read_excel('XXXXXXXX.xlsx') to the correct filename. Hit save then run, 
# Please note only in this file you will have to also modify the names on the csvjson,excel,parquet accoridngly. Takr time to look at the directory. The naming convention of the files should be self explanatory. (The files have been left in the correct format)

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Load the Excel file into a DataFrame
df = pd.read_excel('3monthsTornLogs.xlsx')

# Define lists of keywords for income and expenditure
income_keywords = ["sent", "accepted", "received", "you were paid", "you sold", "You used 18 nerve"]
expenditure_keywords = ["mugged", "assigned", "spent", "you paid", "you bought"]

# Initialize empty columns for income and expenditure
df['Income'] = 0
df['Expenditure'] = 0

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    log = row['Logs'].lower()  # Convert log to lowercase for case-insensitive matching

    # Check for income keywords
    for keyword in income_keywords:
        if keyword in log:
            # Split the log text into words
            words = log.split()
            # Search for the amount starting with '$'
            for word in words:
                if word.startswith('$'):
                    # Extract the amount by removing '$' and commas
                    amount = float(word[1:].replace(',', ''))
                    df.at[index, 'Income'] = amount
                    break  # Exit the loop once amount is found

    # Check for expenditure keywords
    for keyword in expenditure_keywords:
        if keyword in log:
            words = log.split()
            for word in words:
                if word.startswith('$'):
                    amount = float(word[1:].replace(',', ''))
                    df.at[index, 'Expenditure'] = amount
                    break  # Exit the loop once amount is found

# Save the updated DataFrame to a new Excel file
df.to_excel('TornBABMonth1-3.xlsx', index=False)

# Convert the updated DataFrame to CSV
df.to_csv('TornBABMonth1-3.csv', index=False)

# Convert the updated DataFrame to JSON
df.to_json('TornBABMonth1-3.json', orient='records')

# Convert the updated DataFrame to Parquet
table = pa.Table.from_pandas(df)
pq.write_table(table, 'TornBABMonth1-3.parquet')

