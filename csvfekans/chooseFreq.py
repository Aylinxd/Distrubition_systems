import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv('fnew-2023-10.csv') #change name as well

# Filter the DataFrame based on the conditions
df_filtered = df[(df['f'] <= 49.8) | (df['f'] >= 50.2)]

# Convert the 'dtm' column to datetime type
df_filtered['dtm'] = pd.to_datetime(df_filtered['dtm'])

# Extract day from the datetime and create a new column
df_filtered['day'] = df_filtered['dtm'].dt.date

# Group by day and count the number of frequencies
result = df_filtered.groupby('day').size().reset_index(name='count')

result.to_csv('output10.csv', index=False)

print("Process completed. Check 'output10.csv' for the result.")