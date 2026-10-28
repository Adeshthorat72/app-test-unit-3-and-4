import re

# Given text string
text = "The events are scheduled for 25-12-2026, 01-01-2027, and 15-08-2025. Invalid date: 5-6-2024."

# Regular expression to match dates in dd-mm-yyyy format
pattern = r'\b\d{2}-\d{2}-\d{4}\b'

# Find all matching dates
dates = re.findall(pattern, text)

# Display the results
if dates:
    print("Dates found:")
    for date in dates:
        print(date)
else:
    print("No dates found.")
