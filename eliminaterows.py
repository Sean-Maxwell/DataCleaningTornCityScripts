# How to use eliminaterows.py and ExpIncomeCategorisationLogs.py. There are 2 excel files used in the current directory of the these py scripts. Enter the the first file name  xlsx_filename = "XXXXXXXX.xlsx" click save then run.
# See expincome for the last instruction.

import pandas as pd
import re

def load_excel(filename):
    # Load the Excel file into a DataFrame
    return pd.read_excel(filename)

def filter_rows(df, phrases):
    # Define the condition for rows to be eliminated
    condition = df['Logs'].str.contains('|'.join(phrases), case=False, na=False)
    
    # Create a new DataFrame excluding the rows that meet the condition
    return df[~condition]

def remove_dates(df):
    # Define a regex pattern to match dates with timestamps
    date_pattern = r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}'
    
    # Use regex to replace date-time strings with an empty string
    df['Logs'] = df['Logs'].str.replace(date_pattern, '', regex=True)
    
    # Remove commas from the 'Logs' column
    df['Logs'] = df['Logs'].str.replace(',', '')  # Add this line to remove commas
    
    # Remove rows with empty 'Logs' column
    df = df[df['Logs'].str.strip() != '']
    
    return df

def remove_blank_rows(df):
    # Remove rows with all columns containing NaN values
    df = df.dropna(how='all')
    
    return df

def save_to_excel(df, filename):
    # Remove blank rows from the DataFrame
    df = remove_blank_rows(df)
    
    # Save the filtered DataFrame back to the Excel file
    df.to_excel(filename, index=False)
    print("Filtered data (with blank rows removed) saved to Excel file.")

def main():
    xlsx_filename = "3monthsTornLogs.xlsx"  # Replace with your Excel file's name
    phrases_to_exclude = ["You were awarded the honor","rAtAplAn","You were awarded the medal","merits to","You used some Xanax","You were awarded the honor:","and defeated them","You used an Empty Blood Bag","You found","You finished","You joined an official race","You used 150 energy","You used 400 energy","You fitted","similar","MONTHS AGO","MONTH AGO","You updated your profile signature","jail","You boarded"
                          ,"You used some Morphine recovering ","early discharge","to revive you","JFK 2.1's armory","First Aid Kit","Small First Aid Kit","into your Private Island's vault"
                          ,"You were removed from the assault of","passed bot hunter validation","You ate","bailed you out","bust you out","DAY AGO","DAYS AGO","karalynn","You rated", "hospitalized you", "You used a Blood Bag :","Clepto","Huzaifah","You used 4 nerve","revived","You were sent to the hospital","attacked you","you used 5 energy","You used 18 nerve and failed hacking a bank mainframe","You drank","sent a faction newsletter"
                          ,"from your Private Island's vault","You set a new personal best lap","You left an official race","You saved an event","to your enemies list","to your friends list","initiated the plan","You enabled exchanges","You successfully passed authenticator","You added an authorized device","Your maximum life increased","You upgraded your level","You accepted the Duke contract","You completed the Duke contract"
                          ,"You used some Vicodin","You unequipped","You equipped","You read a message","You joined the defense","You were removed from the defense","You changed your revive preference","You loaned","You increased your loan","You decreased your loan","HOURS AGO","You used 2 nerve"] #,,"","","","","","","","",""

    # Load the Excel file
    df = load_excel(xlsx_filename)

    # Remove rows containing dates and commas
    df = remove_dates(df)

    # Filter rows based on the specified phrases
    filtered_df = filter_rows(df, phrases_to_exclude)

    # Save the filtered DataFrame back to the Excel file
    save_to_excel(filtered_df, xlsx_filename)

if __name__ == "__main__":
    main()
