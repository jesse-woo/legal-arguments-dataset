import pandas as pd
from fuzzywuzzy import process

# Set the path to the CSV file
csv_file_path = "annotated-dataset/human-annotated-data-raw.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Standardize values in the 'classification' column to lowercase
data['classification'] = data['classification'].str.lower()

# Define the standard labels for 'classification'
standard_labels = ['affirm', 'grant', 'deny', 'reverse', 'remand', 'defer', 'other']

# Function for fuzzy matching and selecting the best match
def match_label(value):
    match, score = process.extractOne(value, standard_labels)
    return match if score >= 80 else value

# Apply fuzzy matching to the 'classification' column
data['classification'] = data['classification'].apply(match_label)

# Map variations in 'proper_extraction' to True or False
proper_extraction_mapping = {'TRUE': True, 'True': True, 'v': True, 'False': False}
data['proper_extraction'] = data['proper_extraction'].map(proper_extraction_mapping)

# Drop rows with missing values in the 'salience-rating' column
data = data.dropna(subset=['salience-rating'])

# Extract unique values of the 'classification' column after mapping
unique_classification = data['classification'].unique()

# Print the unique standardized values
print("Unique standardized values of 'classification':", unique_classification)

# Save the updated DataFrame to a new CSV file
standardized_file_path = "annotated-dataset/human-annotated-data-standardized.csv"
data.to_csv(standardized_file_path, index=False)

print(f"Data has been standardized and rows without salience rating have been dropped. The updated data is saved to {standardized_file_path}.")
