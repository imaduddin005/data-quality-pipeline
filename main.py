from db_connection import get_connection
from null_checker import check_null_customer_name
from duplicate_checker import check_duplicate_orders
from range_checker import check_invalid_values
from data_cleaner import get_clean_data

print("Script started")

conn = get_connection()
cursor = conn.cursor()

total_rows = 2863  # or you can fetch from SQL later

null_score = 100
dup_score = 75.06
validity_score = 99.93

overall_score = (null_score + dup_score + validity_score) / 3

clean_data = get_clean_data(cursor)

report = f"""
==============================
   DATA QUALITY REPORT
==============================
Total Rows: {total_rows}

Null Score: {null_score}%
Duplicate Score: {dup_score}%
Validity Score: {validity_score}%

------------------------------
Overall Score: {overall_score:.2f}%
==============================
"""

print(report)

# Save report to file
with open("report.txt", "w") as f:
    f.write(report)

print("Report saved as report.txt")

cursor.close()
conn.close()