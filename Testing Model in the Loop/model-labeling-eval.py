import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Set the paths to the CSV files
human_data_path = "../csv-parser/annotated-dataset/human-annotated-data-standardized.csv"
model_outputs_path = "ml_datasets_model_outputs_combined.csv"

# Read the CSV files into DataFrames
human_data = pd.read_csv(human_data_path)
model_outputs = pd.read_csv(model_outputs_path)

# Drop unnecessary columns from the model CSV
model_outputs = model_outputs.drop(['Human Extracted Arguments', 'proper_extraction', 'Human Classifications'], axis=1)

# Merge human classifications with model outputs based on Filing Name
merged_data = pd.merge(human_data, model_outputs, on="Filing Name")

# Define the target column for comparison
target_column = "classification"  # Use the correct column name

# Ensure the specified columns exist in the merged DataFrame
if target_column.lower() not in map(str.lower, merged_data.columns):
    print(f"Error: {target_column} columns not found in the merged dataset.")
    exit()

# Rename columns for clarity
merged_data = merged_data.rename(columns={
    "Mistral Simple Conclusion Category": "Mistral",
    "Llama2 Simple Conclusion Category": "Llama2",
    target_column: "Human"
})

# Remove rows with missing values in the target columns
data_for_evaluation = merged_data.dropna(subset=['Human', 'Mistral', 'Llama2'])

# Get the true labels and predicted labels
true_labels = data_for_evaluation['Human']
predicted_labels_mistral = data_for_evaluation['Mistral']
predicted_labels_llama2 = data_for_evaluation['Llama2']

# Count of rows used
num_rows = len(data_for_evaluation)
print(f"\nNumber of rows used for evaluation: {num_rows}\n")

# Metrics to display
metrics_to_display = ['accuracy', 'precision', 'recall', 'f1-score']

# Evaluate metrics for Mistral
print("Mistral Performance:")
mistral_accuracy = accuracy_score(true_labels, predicted_labels_mistral)
print(f"Accuracy: {mistral_accuracy:.4f}")

# Calculate and print precision, recall, and F1-score
precision, recall, f1, _ = precision_recall_fscore_support(true_labels, predicted_labels_mistral, average='weighted', zero_division=1)
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-score: {f1:.4f}\n")

# Evaluate metrics for Llama2
print("Llama2 Performance:")
llama2_accuracy = accuracy_score(true_labels, predicted_labels_llama2)
print(f"Accuracy: {llama2_accuracy:.4f}")

# Calculate and print precision, recall, and F1-score
precision, recall, f1, _ = precision_recall_fscore_support(true_labels, predicted_labels_llama2, average='weighted', zero_division=1)
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-score: {f1:.4f}")
