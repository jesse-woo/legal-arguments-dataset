import pandas as pd

# Set the path to the standardized CSV file
standardized_file_path = "annotated-dataset/human-annotated-data-standardized.csv"

data = pd.read_csv(standardized_file_path)

numeric_stats = data.describe()

classification_stats = data['classification'].value_counts()
salience_stats = data['salience-rating'].value_counts()

classification_salience_relationship = data.groupby(['classification', 'salience-rating']).size()

# Print the results
print("Descriptive Statistics for Numeric Columns:")
print(numeric_stats)

print("\nClassification Counts:")
print(classification_stats)

print("\nSalience Rating Counts:")
print(salience_stats)

print("\nClassification and Salience Relationship:")
print(classification_salience_relationship)
