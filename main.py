import os
import pandas as pd
import numpy as np

# Extract 30 consecutive data points from each CSV file
def extract_30_consecutive_data_points(file_path, random_seed=42):
    try:
        np.random.seed(random_seed)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path, header=None, parse_dates=[1])

        # Verify that at least 30 data points are available
        if len(df) < 30:
            print(f"File {file_path} does not have enough data points.")
            return None

        # Randomly select a timestamp
        start_index = np.random.randint(0, len(df) - 30)

        # Extract 30 consecutive data points
        data_points = df.iloc[start_index:start_index+30]

        return data_points
    except Exception as e:
        print(f"Error while extracting data points from {file_path}: {e}")
        return None

def detect_outliers(data_points):
    try:
        # Calculate mean and standard deviation of the 30 data points
        mean = data_points[2].mean()
        std_dev = data_points[2].std()

        # Define the threshold for outliers (2 standard deviations beyond the mean)
        threshold = mean + 2 * std_dev

        # Find outliers based on the defined criteria
        outliers = data_points[data_points[2] > threshold].copy()

        # Calculate additional columns
        outliers['Mean'] = mean
        outliers['Actual_Price - Mean'] = outliers[2] - mean
        outliers['% Deviation'] = ((outliers[2] - mean) / mean) * 100

        return outliers
    except Exception as e:
        print(f"Error while detecting outliers: {e}")
        return None

# Main function to process CSV files
def process_csv_files(folder_paths, num_files=2):
    try:
        for folder_path in folder_paths:
            # List CSV files in the directory
            csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

            # Limit the number of files to process based on the input parameter
            num_files = min(num_files, len(csv_files))

            # Process each CSV file
            for file_name in csv_files[:num_files]:
                file_path = os.path.join(folder_path, file_name)

                # Extract data points from the CSV file
                data_points = extract_30_consecutive_data_points(file_path)

                if data_points is not None:
                    # Detect outliers in the extracted data points
                    outliers = detect_outliers(data_points)

                    if outliers is not None and not outliers.empty:
                        # Define the output file path
                        output_file_path = f'{file_name}_outliers.csv'

                        # Write outliers to a new CSV file
                        outliers.to_csv(output_file_path, index=False)
                        print(f"Outliers saved to {output_file_path}")
                    else:
                        print(f"No outliers found in {file_name}")
                else:
                    print(f"Error: Unable to extract data points from {file_name}")
    except Exception as e:
        print(f"Error while processing CSV files: {e}")

# Testing
if __name__ == "__main__":
    nyse_folder = 'NYSE'    # Path to the folder containing NYSE CSV files
    lse_folder = 'LSE'      # Path to the folder containing LSE CSV files
    nasdaq_folder = 'NASDAQ'  # Path to the folder containing NASDAQ CSV files

    # Specify the file names within each folder
    nyse_files = ['ASH.csv', 'NMR.csv']
    lse_files = ['FLTR.csv', 'GSK.csv']
    nasdaq_files = ['TSLA.csv'] 

    # Process each file in the NYSE folder
    for file_name in nyse_files:
        file_path = os.path.join(nyse_folder, file_name)
        data_points = extract_30_consecutive_data_points(file_path)
        if data_points is not None:
            print(f"Data points extracted from {file_name}:\n{data_points}")

    # Process each file in the LSE folder
    for file_name in lse_files:
        file_path = os.path.join(lse_folder, file_name)
        data_points = extract_30_consecutive_data_points(file_path)
        if data_points is not None:
            print(f"Data points extracted from {file_name}:\n{data_points}")
    
    # Process each file in the NASDAQ folder
    for file_name in nasdaq_files:  
        file_path = os.path.join(nasdaq_folder, file_name)
        data_points = extract_30_consecutive_data_points(file_path)
        if data_points is not None:
            print(f"Data points extracted from {file_name}:\n{data_points}")
    
    # Process CSV files from each folder
    process_csv_files([nyse_folder, lse_folder, nasdaq_folder], num_files=2)