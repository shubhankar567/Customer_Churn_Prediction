import os, sys
import pandas as pd
from dataclasses import dataclass #type:ignore
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exceptions import CustomException

# Creating a data class having the configuration details
@dataclass
class DataIngestionConfig:
    raw_file_path = os.path.join('artifacts', 'raw_file.xlsx')
    train_file_path = os.path.join('artifacts', 'train_file.xlsx')
    test_file_path = os.path.join('artifacts', 'test_file.xlsx')

# A class for data ingestion.
class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
    
    # This function will read the data and then split it into test and train and then save it.
    def injectData(self, datafile_path):
        try:
            logging.info('Data Ingestion begins...')
            # Reading th eexcel file
            df = pd.read_excel(datafile_path)

            # Splitting into Independent features (X) and target variable (y)
            X = df.drop('Churn', axis = 1)
            y = df[['Churn']]

            # Performing a train-test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=40, test_size=0.3)

            # Again concating the X and y of train and test data to make two complete datasets
            train_df = pd.concat([X_train, y_train], axis = 1)
            test_df = pd.concat([X_test, y_test], axis = 1)

            df.to_excel(self.config.raw_file_path, index = False)
            train_df.to_excel(self.config.train_file_path, index = False)
            test_df.to_excel(self.config.test_file_path, index = False)

            logging.info(f'Datafiles are succcesfully stored in {os.path.dirname(self.config.raw_file_path)} folder.')
            return self.config.raw_file_path, self.config.train_file_path, self.config.test_file_path
        
        except Exception as e:
            logging.info('Error occured while reading the data files.')
            raise CustomException(e, sys) #type:ignore