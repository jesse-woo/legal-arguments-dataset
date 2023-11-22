import pandas as pd
import re

def extract_table_of_contents(text):
    contents = re.findall(r'\b(\w+\s*\.*\s*\w*)\.*\s+(\d+)', text)
    return dict(contents)

def extract_conclusion(text):
    if pd.isna(text):  # Check if the value is NaN
        return ""
    return str(text).strip()


def analyze_outcome(contents, conclusion, human_annotation=None):
    outcome_keywords = {
        'affirm': ['affirm', 'uphold'],
        'reverse': ['reverse', 'overturn'],
        'remand': ['remand', 'send back'],
        'grant': ['grant', 'approve'],
        'deny': ['deny', 'reject']
    }

    if human_annotation:
        return human_annotation

    toc_topics = ' '.join(contents.keys()).lower()
    conclusion_text = conclusion.lower()

    for outcome, keywords in outcome_keywords.items():
        for keyword in keywords:
            if keyword in toc_topics or keyword in conclusion_text:
                return outcome

    return 'other'

def process_csv(csv_path):
    df = pd.read_csv(csv_path)
    df.style

    # Add new columns for extracted data
    df['Table of Contents'] = df['Extracted Table of Contents'].apply(extract_table_of_contents)
    df['Conclusion'] = df['Conclusion'].apply(extract_conclusion)

    # Add a new column for human annotation (you can replace 'None' with actual annotations)
    df['Human Annotation'] = None

    # Add a new column for outcome analysis
    df['Outcome'] = df.apply(lambda row: analyze_outcome(row['Table of Contents'], row['Conclusion'], row['Human Annotation']), axis=1)

    return df

if __name__ == "__main__":
    csv_path = 'extracted_toc_with_conclusion.csv'  # Replace with the actual path to your CSV file
    processed_df = process_csv(csv_path)

    # Display the processed DataFrame
    print(processed_df)


    # Save the DataFrame to a new CSV file
    processed_df.to_csv('output_with_outcome_analysis_and_annotation.csv', index=False)
