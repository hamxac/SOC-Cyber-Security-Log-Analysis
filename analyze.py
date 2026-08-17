import pandas as pd

# 1. Load the data again
df = pd.read_csv('auth_logs.csv')

# 2. Filter for only the failed attempts
failed_attempts = df[df['status'] == 'failed']
print("\n--- ONLY FAILED LOGINS ---")
print(failed_attempts)

# 3. Count which IP address is failing the most
print("\n--- SUSPICIOUS IP COUNT ---")
hacker_count = failed_attempts['ip_address'].value_counts()
print(hacker_count)