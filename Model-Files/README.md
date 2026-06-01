# Model Files

This folder contains all saved machine learning artifacts required for prediction and deployment.

## Files

### model.pkl

Trained machine learning model used for winner prediction.

### scaler.pkl

StandardScaler object used for feature scaling.

### columns.pkl

Stores feature column structure used during training to ensure consistent preprocessing during prediction.

## Purpose

These files allow the deployment application to:

* Load the trained model
* Apply the same preprocessing pipeline
* Generate predictions for new IPL matches

The files were created using Python Pickle serialization.

