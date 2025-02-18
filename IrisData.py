import pandas as pd

# Load the dataset
df = pd.read_csv("Iris.csv")  # Make sure the file is in the same folder as your script

# Keep only numeric columns (remove ID, species, or any non-numeric data)
numeric_df = df.select_dtypes(include=['number'])

# Normalize the data (scaling values between 0 and 1)
normalized_df = (numeric_df - numeric_df.min()) / (numeric_df.max() - numeric_df.min())

# Standardize the data (mean = 0, standard deviation = 1)
standardized_df = (numeric_df - numeric_df.mean()) / numeric_df.std()

# Save the new datasets
normalized_df.to_csv("Iris_normalized.csv", index=False)
standardized_df.to_csv("Iris_standardized.csv", index=False)

print("Files saved: Iris_normalized.csv and Iris_standardized.csv")