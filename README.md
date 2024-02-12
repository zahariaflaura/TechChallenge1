# TechChallenge1

This Python script is designed to detect outliers in time series data from CSV files using the Visual Studio Code (VS Code) editor and various Python libraries including pandas, NumPy, and os.

Description
The script consists of two main functions:

extract_30_consecutive_data_points(file_path, random_seed=42): This function extracts 30 consecutive data points from each CSV file provided. It utilizes pandas for data manipulation and NumPy for random number generation.

detect_outliers(data_points): This function identifies outliers in the extracted data points based on a predefined threshold. It computes the mean and standard deviation of the data points using NumPy and detects outliers that exceed 2 standard deviations from the mean.

Additionally, the script includes a main function process_csv_files(folder_paths, num_files=2) to process CSV files from specified folders, extract data points, detect outliers, and save the results to new CSV files.

The script includes error handling to gracefully manage exceptions such as missing files, insufficient data points, and invalid file formats.

Libraries Used
pandas: For data manipulation and CSV file handling.
NumPy: For numerical computing and random number generation.
os: For operating system dependent functionality, such as file path handling.

Usage
To use the script:

1. Install Python and the required libraries (pandas, NumPy).
2. Ensure the CSV files are organized in folders according to the specified file paths.
3. Execute the script in a Python environment.

Note
Ensure that the CSV files contain the necessary data in the specified format and that the file paths are correctly set before running the script.
