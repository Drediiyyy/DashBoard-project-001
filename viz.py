import pandas as pd
import plotly.express as px
import os

# Create output folder if it doesn't exist
os.makedirs("../outputs", exist_ok=True)

# Load the data
df = pd.read_csv('../data/regional_sales.csv')

# Create the dashboard chart
fig = px.bar(df, x='Region', y='Sales', title='Regional Sales Dashboard')

# Save the outputs
fig.write_html("../outputs/dashboard.html")
fig.write_image("../outputs/screenshot.png")

print("✅ Dashboard saved as HTML and PNG in /outputs/")
