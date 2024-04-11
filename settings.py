# settings.py

# Path settings
HEALTHY_PLANTS_DIR = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/Healthy Plants/Raw_Healthy'
INFECTED_PLANTS_DIR = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/Infected Plants/Infected_Raw'
PROCESSED_HEALTHY_DIR = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/Healthy Plants/Pre-processed_Healthy'
PROCESSED_INFECTED_DIR = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/Infected Plants/Pre-processed_Infected'
FEATURES_DIR = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/other/Features'  #features as files
MODEL_DIR = '~/Documents/GitHub/Computer-Graphics-Automated-Detection/other/Modles'  # save models

# Ensure that the necessary directories exist
import os
os.makedirs(PROCESSED_HEALTHY_DIR, exist_ok=True)
os.makedirs(PROCESSED_INFECTED_DIR, exist_ok=True)
os.makedirs(FEATURES_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# Preprocessing settings
GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
MORPHOLOGICAL_KERNEL_SIZE = (5, 5)
HISTOGRAM_BINS = 256
HISTOGRAM_RANGE = (0, 256)

# Feature extraction settings
LBP_RADIUS = 3
LBP_POINTS = 24
LBP_METHOD = 'uniform'

# Classifier settings
CLASSIFIER_TYPE = 'RandomForest'  # Could be 'SVM', 'DecisionTree', 'RandomForest', etc.
SVM_C = 1.0
SVM_KERNEL = 'rbf'
DECISION_TREE_DEPTH = None
RANDOM_FOREST_ESTIMATORS = 100
RANDOM_FOREST_MAX_DEPTH = None

# Training settings
TEST_SIZE = 0.2
RANDOM_STATE = 42

# Evaluation settings
EVALUATION_METRICS = ['accuracy', 'precision', 'recall', 'f1-score']
