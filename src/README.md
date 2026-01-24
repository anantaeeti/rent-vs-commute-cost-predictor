📁 src/ — Development & Experimentation
This folder contains the development-stage scripts used to build the final deployed application.
These files represent the complete machine learning workflow prior to deployment.
📄 create_dataset.py
Generates a synthetic but realistic dataset for life cost prediction based on rent and commute time.
Controlled noise is added to simulate real-world variability.
📄 explore_dataset.py
Performs exploratory data analysis (EDA) to:
Understand feature distributions
Visualize relationships between rent, commute, and life cost
Validate assumptions before modeling
📄 linear_regression.py
Implements Linear Regression using Gradient Descent to:
Train the model
Analyze residuals
Extract interpretable coefficients
The final trained parameters from this script are used in the deployed Streamlit app.
🚀 Deployment Note
The production application (app.py) uses the trained parameters obtained from this pipeline.
The scripts in this folder are not executed during deployment.
