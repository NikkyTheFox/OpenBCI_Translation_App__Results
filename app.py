import pandas as pd

# 250Hz => 4 entries pre second

# PLACEHOLDER 
# recordings\day2\1734701913.csv

file_path = 'recordings/day2/1734701913.csv'
df = pd.read_csv(file_path)

df['State'] = 'R'

df.loc[100:, 'State'] = 'F'

output_file = 'manually_labeled/day2/1734701913.csv'
df.to_csv(output_file, index=False)

print(f"Updated CSV file saved to {output_file}")
