import cv2
import os
from skimage import exposure
import numpy as np
from settings import HEALTHY_PLANTS_DIR, INFECTED_PLANTS_DIR

# Add your preprocessing steps here
def preprocess_image(image):
    # Convert to grayscale, apply Gaussian blur, etc.
    # Return the preprocessed image
    pass

# Function to handle preprocessing for a single category (Healthy or Infected)
def preprocess_dataset(image_directory, processed_directory):
    for filename in os.listdir(image_directory):
        if filename.lower().endswith('.jpg'):  # Check for JPEG images
            image_path = os.path.join(image_directory, filename)
            processed_image_path = os.path.join(processed_directory, filename)

            # Read image
            image = cv2.imread(image_path, cv2.IMREAD_COLOR)

            # Preprocess the image
            processed_image = preprocess_image(image)

            # Save the processed image
            cv2.imwrite(processed_image_path, processed_image)

# Define your paths
healthy_plants_directory = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/Healthy Plants/Raw_Healthy'
infected_plants_directory = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/Infected Plants/Infected_Raw'
processed_healthy_directory = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/Healthy Plants/Pre-processed_Healthy'
processed_infected_directory = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/Infected Plants/Pre-processed_Infected'

# Create directories for processed images if they don't exist
os.makedirs(processed_healthy_directory, exist_ok=True)
os.makedirs(processed_infected_directory, exist_ok=True)

# Preprocess healthy plant images
preprocess_dataset(healthy_plants_directory, processed_healthy_directory)

# Preprocess infected plant images
preprocess_dataset(infected_plants_directory, processed_infected_directory)
