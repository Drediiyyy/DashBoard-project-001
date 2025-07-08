import pandas as pd
import numpy as np
import os

# Create output directory if it doesn't exist
os.makedirs("../data", exist_ok=True)

# Generate dummy sales data
regions = ['North America', 'Europe', 'Asia', 'South America', 'Africa']
sales = np.random.randint(50000, 150000, size=len(regions))

df = pd.DataFrame({
    'Region': regions,
    'Sales': sales
})

# Save to CSV
df.to_csv('../data/regional_sales.csv', index=False)
print("✅ Data saved to ../data/regional_sales.csv")
