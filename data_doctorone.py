import pandas as pd

# Load dataset
data = pd.read_excel("dirty_dataset.xlsx.xlsx")

print("Original Dataset:\n", data)

# Handle missing values
data["Marks"].fillna(data["Marks"].mean(), inplace=True)

# Remove duplicates
data = data.drop_duplicates()

# Standardize text (make city lowercase)
data["City"] = data["City"].str.lower()

print("\nCleaned Dataset:\n", data)