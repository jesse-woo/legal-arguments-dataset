import os
import pandas as pd

# Set the path to the folder containing CSV files
folder_path = "human-annotated-data/"

# Initialize an empty list to store individual DataFrames
dfs = []

# Iterate through all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        
        # Read each CSV file into a DataFrame and append to the list
        current_data = pd.read_csv(file_path)
        print(f"File {file_path} has been read and added")
        dfs.append(current_data)

# Concatenate all DataFrames in the list into one DataFrame
combined_data = pd.concat(dfs, ignore_index=True)

# Keep only the specified headers in the target DataFrame
target_headers = ["Filing Name", "URL", "proper_extraction", "classification", "salience-rating", "annotator-uni"]
combined_data = combined_data[target_headers]

# Save the combined data to a new CSV file in the "annotated-dataset/" folder
output_folder = "annotated-dataset/"
os.makedirs(output_folder, exist_ok=True)
output_file_path = os.path.join(output_folder, "human-annotated-data-raw.csv")
combined_data.to_csv(output_file_path, index=False)

print(f"Data has been successfully scraped and saved to {output_file_path}.")
