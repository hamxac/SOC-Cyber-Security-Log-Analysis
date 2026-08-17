import pandas as pd

print("Loading raw data...")
df = pd.read_csv('real_logs.csv')

# 1. Tell Python which columns to KEEP (we are throwing away the rest)
columns_to_keep = [
    'Timestamp', 'Source IP Address', 'Destination IP Address', 
    'Protocol', 'Attack Type', 'Action Taken', 
    'Severity Level', 'Geo-location Data'
]

# Create a new table with only those columns
clean_df = df[columns_to_keep]

# 2. Rename the columns so SQL doesn't get confused by the spaces
clean_df.columns = [
    'timestamp', 'source_ip', 'destination_ip', 
    'protocol', 'attack_type', 'action_taken', 
    'severity_level', 'geo_location'
]

# 3. Save this perfect data as a brand new CSV file
print("Saving cleaned data...")
# index=False just prevents Pandas from adding a useless row number column
clean_df.to_csv('clean_logs.csv', index=False) 

print("Success! Data is cleaned and saved as clean_logs.csv")