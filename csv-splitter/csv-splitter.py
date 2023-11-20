import pandas as pd
import os

def split_csv(input_csv, output_directory, annotators_file):
    # Read the original CSV file
    df = pd.read_csv(input_csv)

    # Read the annotators file to get the list of UNIs
    with open(annotators_file, 'r') as f:
        annotators = [uni.strip() for uni in f.readlines()[1:]]

    # Ensure output directory exists, create if not
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Calculate the number of rows in each piece
    rows_per_piece = len(df) // len(annotators)

    # Check if there are enough rows in the parent CSV given the number of UNIs
    if rows_per_piece < 10:
        print("Error: Not enough rows in the parent CSV to meet the specified constraints.")
        return

    # Add new columns to the original dataframe
    new_columns = ['proper_extraction', 'classification', 'salience-rating', 'annotator-uni']
    df = pd.concat([df, pd.DataFrame(columns=new_columns)], axis=1)

    # Split the original dataframe for each annotator using index and offset
    for i, uni in enumerate(annotators):
        # Calculate the offset for the current annotator
        offset = i * rows_per_piece

        # Determine the number of rows for the current piece
        piece_rows = min(20, rows_per_piece)  # Set to exactly 20 or the remaining rows if less

        # Write the piece to a new CSV file
        output_file = os.path.join(output_directory, f"{uni}.csv")
        df.iloc[offset:offset + piece_rows, -1] = uni  # Set 'annotator-uni' column
        df.iloc[offset:offset + piece_rows].to_csv(output_file, index=False)

        print(f"CSV file created for {uni}: {output_file}, Rows written: {piece_rows}")

if __name__ == "__main__":
    # Specify the input CSV file, output directory, and annotators file
    input_csv = "input/output_with_outcome_analysis.csv"
    output_directory = "output/"
    annotators_file = "annotators.txt"

    # Call the function to split the CSV
    split_csv(input_csv, output_directory, annotators_file)
