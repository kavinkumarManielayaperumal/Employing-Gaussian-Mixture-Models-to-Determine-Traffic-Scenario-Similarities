
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')


# Define the file path for the input CSV file
file_path = r'F:\gaussian mixture\standardized_data\features for the ego vehicle.csv'

# Load the dataset
data = pd.read_csv(file_path)

# Columns to standardize
columns_to_standardize = ['x', 'y', 'xVelocity', 'yVelocity', 'xAcceleration', 'yAcceleration','frontSightDistance','backSightDistance','precedingXVelocity']

# Compute mean and standard deviation for the selected columns
mean_std = data[columns_to_standardize].agg(['mean', 'std'])

# Standardize the selected columns using Z-score formula
data_standardized = data.copy()
for col in columns_to_standardize:
    data_standardized[col] = (data[col] - mean_std.loc['mean', col]) / mean_std.loc['std', col]

# Print the first few rows of the standardized dataset (for verification)
print(data_standardized.head())

# Define the output directory and file path
output_folder = r'F:\gaussian mixture\standardized_data'
output_file_path = os.path.join(output_folder, 'standardized_01_tracks_and_additional_features.csv')

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created new folder: {output_folder}")

# Save the standardized dataset to a new CSV file
data_standardized.to_csv(output_file_path, index=False)
print(f"Standardized data saved to: {output_file_path}")