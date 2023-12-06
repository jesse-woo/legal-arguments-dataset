import pandas as pd

# Set the path to the CSV file
csv_file_path = "annotated-dataset/human-annotated-data-raw.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Standardize values in the 'classification' column to lowercase
data['classification'] = data['classification'].str.lower()

# Extract unique values of the 'classification' column after standardization
unique_classification = data['classification'].unique()

# Print the unique standardized values
print("Unique standardized values of 'classification':", unique_classification)

# Save the updated DataFrame to a new CSV file
standardized_file_path = "annotated-dataset/human-annotated-data-standardized.csv"
data.to_csv(standardized_file_path, index=False)

print(f"Data has been standardized and saved to {standardized_file_path}.")
