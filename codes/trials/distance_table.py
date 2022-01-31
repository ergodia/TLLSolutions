"""
distance_table.py

- Reads distance CSV file into a dataframe
- Converts dataframe to a distance table
- Saves results to CSV file

"""

import pandas as pd

# Read data
df_1 = pd.read_csv( '../../data/ConnectiesNationaal.csv')

# Rename columns
df_2 = df_1.rename(columns={'station1': 'station2', 'station2': 'station1'} )
df_2 = df_2[['station1', 'station2', 'distance']]

# Concat dataframes
frames = [df_1, df_2]
result = pd.concat(frames)

# Transform dataframe to distance table
matrix_df = result.pivot_table(index='station1', columns='station2', values='distance')

# Add column with number of connections per station
matrix_df['connections'] = matrix_df.count()
matrix_df.fillna(0, inplace =True)

print(matrix_df)

# Calculate total connections
total = matrix_df['connections'].sum()

# Divide total by 2 (they occur twice in the table)
print('Aantal connections:', total/2)

# Write dataframe into CSV file
matrix_df.to_csv('../../data/DistanceTable_NL.csv')