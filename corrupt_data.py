import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("superstore.csv", encoding='latin1')

print("Original Shape:", df.shape)

# -------------------------
# INTENTIONALLY CORRUPT DATA
# -------------------------

# 1. Missing values (NULL)
df.loc[5, 'Customer Name'] = np.nan
df.loc[12, 'Sales'] = np.nan
df.loc[20, 'Category'] = np.nan

# 2. Negative values (invalid range)
df.loc[30, 'Sales'] = -500
df.loc[35, 'Quantity'] = -10

# 3. Wrong category typo
df.loc[40, 'Category'] = 'Furnture'
df.loc[45, 'Category'] = 'Techology'

# 4. Duplicate rows
duplicate_row = df.iloc[50]
df = pd.concat([df, duplicate_row.to_frame().T],
               ignore_index=True)

duplicate_row2 = df.iloc[60]
df = pd.concat([df, duplicate_row2.to_frame().T],
               ignore_index=True)

# 5. Invalid date
df.loc[70, 'Order Date'] = '2026-99-45'

# 6. Wrong datatype
df.loc[80, 'Sales'] = 'abc'

# 7. Outlier value
df.loc[90, 'Sales'] = 99999999

# Save corrupted dataset
df.to_csv("corrupted_superstore.csv", index=False)

print("Corrupted dataset created successfully!")
print("New Shape:", df.shape)