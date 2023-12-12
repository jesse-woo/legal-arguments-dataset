import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Get the total count for each classification type
total_classification_count = len(data)

# Visualize the distribution of each classification type and save as an image
fig_classification = plt.figure(figsize=(10, 6))
ax_classification = sns.countplot(x='classification', data=data, order=data['classification'].value_counts().index)
plt.title('Distribution of Classification Types')
plt.xlabel('Classification Types')
plt.ylabel('Count')

# Annotate count values on top of each bar
for p in ax_classification.patches:
    ax_classification.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Add a text annotation for the total count
plt.text(0.5, -0.1, f'Total N = {total_classification_count}', ha='center', va='center', transform=ax_classification.transAxes)

fig_classification.savefig("classification_distribution.png")

# Get the total count for each salience rating
total_salience_count = len(data)

# Visualize the distribution of each salience rating and save as an image
fig_salience = plt.figure(figsize=(10, 6))
ax_salience = sns.countplot(x='salience-rating', data=data, order=data['salience-rating'].value_counts().index)
plt.title('Distribution of Salience Ratings')
plt.xlabel('Salience Ratings')
plt.ylabel('Count')

# Annotate count values on top of each bar
for p in ax_salience.patches:
    ax_salience.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Add a text annotation for the total count
plt.text(0.5, -0.1, f'Total N = {total_salience_count}', ha='center', va='center', transform=ax_salience.transAxes)

fig_salience.savefig("salience_distribution.png")
