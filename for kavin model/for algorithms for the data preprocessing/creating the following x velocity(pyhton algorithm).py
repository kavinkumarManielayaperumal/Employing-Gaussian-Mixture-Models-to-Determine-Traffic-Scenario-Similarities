import pandas as pd

# Load your dataset
file_path = "F:\gaussian mixture\standardized_data\standaedized for the addtioal features with perceding x velocity and following x velocity\01_tracks.csv"# Replace with the actual path
data = pd.read_csv(file_path)

# Create a column for following x-velocity
data['following_x_velocity'] = 0  # Initialize with zero

# Calculate following x-velocity based on following ID
for index, row in data.iterrows():
    following_id = row['followingId']
    frame = row['frame']
    
    if following_id > 0:  # Check if there is a following vehicle
        # Find the row corresponding to the following vehicle in the same frame
        following_row = data[(data['id'] == following_id) & (data['frame'] == frame)]
        
        if not following_row.empty:
            # Assign the x-velocity of the following vehicle
            data.at[index, 'following_x_velocity'] = following_row['xVelocity'].values[0]

# Save the updated dataset
output_path = "updated_dataset_with_following_x_velocity.csv"  # Replace with desired output path
data.to_csv(output_path, index=False)

print("Following X-Velocity column calculated and saved.")
