import csv
import pandas as pd

# Load your original CSV
input_file = "courses2025.csv"
output_file = "courses2025_cleaned.csv"

# Read and write using pandas for safety (but enforce quoting using csv module)
df = pd.read_csv(input_file)

# Write to a new CSV with all fields quoted
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=df.columns, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in df.to_dict(orient='records'):
        writer.writerow(row)

print("CSV cleaned and quoted successfully:", output_file)
