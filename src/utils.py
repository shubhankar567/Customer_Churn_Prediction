# Importing necessary libraries and modules
from sklearn.metrics import accuracy_score, precision_score, recall_score
from src.logger import logging
from src.exceptions import CustomException
import pickle #type:ignore
import os, sys

def load_pkl(pkl_path):
    '''Function for loading a pickle file from the path given as input.'''
    try:
        with open(pkl_path, 'rb') as pkl_obj:
            file = pickle.load(pkl_obj)
        logging.info(f'{pkl_path} loaded successfully')
        return file
    except Exception as e:
        logging.info(f'Exception occured during loading {pkl_path}')
        raise CustomException(e, sys)

def save_pkl(pkl_path, pkl_file):
    '''Function for saving a pickle file to the path given as input.'''
    try: 
        os.makedirs(os.path.dirname(pkl_path), exist_ok=True)
        with open(pkl_path, 'wb') as pkl_obj:
            pickle.dump(pkl_file, pkl_obj)
        logging.info(f'Pickle file succesfully dumped at {pkl_path}')

    except Exception as e:
        logging.info(f'Error occured while saving the pickle file at {pkl_path}')
        raise CustomException(e, sys)

def evaluate_model(X_train, X_test, y_train, y_test, models):
    '''Function to evaluate all the models simultaneoudly and give the metrics for all of them'''
    try:
        assessment = {}
        y_test = y_test.values.ravel()
        y_train = y_train.values.ravel()
        for model_name in models:
            model = models[model_name]
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            assessment[model_name] = {
                'Accuracy': accuracy,
                'Precision': precision,
                'Recall': recall
            } 
        return assessment
    
    except Exception as e:
        logging.info('Error while evaluating models.')
        raise CustomException(e, sys)
