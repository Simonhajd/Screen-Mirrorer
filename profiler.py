import pstats
import pandas as pd
import matplotlib.pyplot as plt

# Read the profiling results
p = pstats.Stats('profile_results.out')

# Convert the stats to a pandas DataFrame
df = pd.DataFrame(p.stats.items(), columns=['func', 'stats'])

# Extract the function names
df['func_name'] = df['func'].apply(lambda x: x[2])

# Extract the total time per function
df['total_time'] = df['stats'].apply(lambda x: x[2])

# Sort the DataFrame by total time
df = df.sort_values('total_time', ascending=False)

# Exclude the two longest results
df = df.iloc[:-2]

# Plot the results
plt.barh(df['func_name'], df['total_time'])
plt.xlabel('Total Time')
plt.ylabel('Function')
plt.title('Profiling Results')
plt.show()