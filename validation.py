import pandas as pd

df = pd.read_csv("heart.csv")

print("Missing Value Validation")
print("-" * 35)

missing_values = df.isnull().sum()

for column, value in missing_values.items():
    if value == 0:
        print(f"{column}: No missing values")
    else:
        print(f"{column}: {value} missing value(s)")
