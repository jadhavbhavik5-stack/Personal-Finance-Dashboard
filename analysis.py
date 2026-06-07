# import pandas as pd
# import matplotlib.pyplot as plt

# print("Everything works!")
# ------------------------
# import pandas as pd

# df = pd.read_csv("fraudtrain.csv")

# print(df.shape)
# print(df.head())
# ------------------

# import pandas as pd

# df = pd.read_csv("fraudtrain.csv")

# print(df.columns)

import pandas as pd

df = pd.read_csv("fraudtrain.csv")

# print(df.shape)
# print(df.head())
# print(df.columns)

# print(df.isnull().sum())

# Drop useless columns
columns_to_drop = ['Unnamed: 0', 'cc_num', 'trans_num', 'unix_time', 
                   'street', 'zip', 'lat', 'long', 'merch_lat', 'merch_long']

df = df.drop(columns=columns_to_drop)

# print(df.columns)

# Convert date column from text to actual date format
df['trans_date_trans_time'] = pd.to_datetime(df['trans_date_trans_time'])

# Extract month and year into separate columns
df['month'] = df['trans_date_trans_time'].dt.month
df['year'] = df['trans_date_trans_time'].dt.year

# print(df[['trans_date_trans_time', 'month', 'year']].head())

# Convert dob from text to date format
df['dob'] = pd.to_datetime(df['dob'])

# Calculate age
df['age'] = df['year'] - df['dob'].dt.year

# print(df[['dob', 'age']].head())

# Save cleaned data to a new file
df.to_csv("cleaned_transactions.csv", index=False)

print("File saved successfully!")


