import pandas as pd

# Load the data
df = pd.read_csv('real_logs.csv')

print("\n--- ALL 25 COLUMN NAMES ---")
# This prints out a clean list of every column we have to work with
print(df.columns.tolist())

print("\n--- MISSING DATA CHECK ---")
# This scans the entire dataset and counts the blank/empty cells
print(df.isnull().sum())