import pandas as pd

def flip_backwards_to_forward(data):
    # Loop through the dataframe
    for index, row in data.iterrows():
        # Check if the vehicle is moving backward (negative velocity and acceleration)
        if row['xVelocity'] < 0:
            # Flip the velocity and acceleration to positive
            data.at[index, 'xVelocity'] = abs(row['xVelocity'])
            data.at[index, 'xAcceleration'] = abs(row['xAcceleration'])
            
        if row['yVelocity'] < 0:
            # Flip the y-velocity and y-acceleration to positive
            data.at[index, 'yVelocity'] = abs(row['yVelocity'])
            data.at[index, 'yAcceleration'] = abs(row['yAcceleration'])
    
    return data

# Load your CSV
file_path = r'F:\gaussian mixture\standardized_data\flipping the direction of the vehical, scritp for the python\01_tracks.csv'

data = pd.read_csv(file_path)

# Apply the function to flip backward vehicles to forward motion
data = flip_backwards_to_forward(data)

# Save the modified dataset to a new CSV file
data.to_csv('F:\gaussian mixture\standardized_data\modified_file.csv', index=False)

print("File with flipped backward vehicle values saved as 'modified_file.csv'")



