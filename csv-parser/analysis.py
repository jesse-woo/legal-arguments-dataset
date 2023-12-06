import pandas as pd

# Set the path to the CSV file
csv_file_path = "annotated-dataset/human-annotated-data-raw.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(csv_file_path)

# Extract unique values of specified columns
unique_proper_extraction = data["proper_extraction"].unique()
unique_classification = data["classification"].unique()
unique_salience_rating = data["salience-rating"].unique()

# Print the unique values
print("Unique values of 'proper_extraction':", unique_proper_extraction)
print("Unique values of 'classification':", unique_classification)
print("Unique values of 'salience-rating':", unique_salience_rating)
