import pandas as pd

print("Loading massive dataset. This might take a second...")
# Load the new, large dataset
df = pd.read_csv('real_logs.csv')

print("\n--- DATASET SIZE ---")
# .shape tells you exactly how many rows and columns are in the file
print(df.shape) 

print("\n--- FIRST 5 ROWS ---")
# .head() prints the first 5 rows so we can see what the data looks like
print(df.head())