# Customer Churn Prediction System

The Customer Churn Prediction System is a project that aims to predict customer churn in a business based on various input features such as Age, Gender, Location, Subscription_Length_Months, Monthly_Bill, Total_Usage_GB. This system deploys various machine learning models, including Logistic Regression, Support Vector Classifier (SVC), Decision Tree Classifier, Random Forest Classifier, XGBoost, Naive Bayes Classifier, and Artificial Neural Networks (ANN) with 100 epochs. After comprehensive evaluation, the **Decision Tree Classifier** emerged as the best-performing model with the highest accuracy and recall values for predicting customer churn.

## Project Structure

The project is organized into the following main components:

1. **src Folder**

   This folder contains the core source code for the Customer Churn Prediction System.

   - `exceptions.py`: This module handles custom exceptions for the project.
   - `logger.py`: It provides a logging utility to log events during the execution of the system.
   - `utils.py`: Contains utility functions used across the project.

2. **components Folder**

   - `data_ingestion.py`: Handles the loading of input data for training and prediction.
   - `data_transformation.py`: Performs data preprocessing and transformation tasks.
   - `model_training.py`: Implements the training of the Decision Tree Classifier model.

3. **pipelines Folder**

   - `train_pipeline.py`: Initiates the entire training process, including data ingestion, preprocessing, and model training. The trained model is then saved in the artifacts folder.
   - `predict_pipeline.py`: Loads the trained model and makes predictions based on new customer data.

4. **setup.py**

   The setup.py file contains configuration details about the Customer Churn Prediction System.

5. **requirements.txt**

   The requirements.txt file lists all the required libraries and dependencies for running the project. Ensure you install these dependencies before executing the system.

6. **artifacts Folder**

   The artifacts folder is used to store model files, including the trained Decision Tree Classifier model.

7. **notebooks Folder**

   The notebooks folder contains Jupyter notebooks used for exploratory data analysis (EDA) and experimentation during the development of the project.

8. **application.py**

   The application.py file acts as a Flask web application that provides a user-friendly interface for users to input customer characteristics and receive churn predictions based on the trained model.

## Dependencies

The Customer Churn Prediction System relies on the following libraries:

- scikit-learn (sklearn)
- Python
- NumPy
- Pandas
- Seaborn
- Flask
- tensorflow
- openpyxl

## Getting Started

To run the Customer Churn Prediction System, follow these steps:

1. Install the required dependencies listed in requirements.txt.

2. Run the `train_pipeline.py` file to train the model and generate the necessary artifacts.

3. After successful training, run the `application.py` file to launch the Flask web application.

4. Access the application in your web browser, provide customer characteristics as input, and get the predicted churn status.

## Contribution

Contributions to the Customer Churn Prediction System are welcome. If you find any issues or have suggestions for improvement, feel free to submit a pull request or open an issue.

Happy predicting!