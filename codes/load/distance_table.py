"""
distance_table.py

- reads distance CSV file into a dataframe
- converts dataframe to a distance table
- saves results to CSV file
"""

import pandas as pd

# read data
df_1 = pd.read_csv( '../../data/ConnectiesNationaal.csv')

# rename columns
df_2 = df_1.rename(columns={'station1': 'station2', 'station2': 'station1'} )
df_2 = df_2[['station1', 'station2', 'distance']]

# concat dataframes
frames = [df_1, df_2]
result = pd.concat(frames)

# transform dataframe to distance table
matrix_df = result.pivot_table(index='station1', columns='station2', values='distance')

# add column with number of connections per station
matrix_df['connections'] = matrix_df.count()
matrix_df.fillna(0, inplace =True)

print(matrix_df)

# calculate total connections
total = matrix_df['connections'].sum()

# divide total by 2 (they occur twice in the table)
print('Aantal connections:', total/2)

# write dataframe into CSV file
matrix_df.to_csv('../../data/DistanceTable_NL.csv')
