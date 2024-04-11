import os
from settings import HEALTHY_PLANTS_DIR, INFECTED_PLANTS_DIR
from functions import preprocess_dataset, healthy_plants_directory, infected_plants_directory, processed_healthy_directory, processed_infected_directory

# Start preprocessing of healthy plant images
preprocess_dataset(healthy_plants_directory, processed_healthy_directory)

# Start preprocessing of infected plant images
preprocess_dataset(infected_plants_directory, processed_infected_directory)

# Step 2: Feature Extraction
# Extract features and labels, and store them in X and y respectively
X, y = [], []
for category, directory in [('healthy', processed_healthy_directory), ('infected', processed_infected_directory)]:
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Assume 'extract_features' is a function that takes a file path and returns a feature array
        features = extract_features(file_path)
        X.append(features)
        y.append(0 if category == 'healthy' else 1)  # Label healthy as 0 and infected as 1

# Step 3: Splitting the Dataset
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Training the Classifier
# Assume 'train_classifier' is a function that takes training data and returns a trained model
classifier = train_classifier(X_train, y_train)

# Step 5: Evaluating the Classifier
# Assume 'evaluate_classifier' is a function that takes a model, test data, and test labels, then prints evaluation metrics
evaluate_classifier(classifier, X_test, y_test)

# If you want to save the trained model, use joblib or pickle to serialize it
import joblib
joblib.dump(classifier, '/Users/hernerdez/Documents/GitHub/Computer-Graphics-Automated-Detection/other')

# To load the model later:
# classifier = joblib.load('/Users/hernerdez/Documents/GitHub/Computer-Graphics-Automated-Detection/other')