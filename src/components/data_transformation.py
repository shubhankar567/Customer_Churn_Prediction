import os, sys #type:ignore
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_pkl
from dataclasses import dataclass #type:ignore

@dataclass
class DataTransformationConfig:
    pkl_path = os.path.join('artifacts', 'transformer.pkl')

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()
    
    # A function for getting transformer object
    def get_transformer(self):
        logging.info('Creating the transformer object')
        # Defining the numerical columns
        num_columns = ['Age', 'Subscription_Length_Months', 'Monthly_Bill', 'Total_Usage_GB']

        # Creating a pipeline for numerical columns
        num_pipe = Pipeline(
            steps = [
                ('Imputer', SimpleImputer(strategy='mean')),
                ('Scaler', StandardScaler())
            ]
        )

        # Creating a pipeline for Location column
        hotEncode_pipe = Pipeline(
            steps = [
                ('oneHot', OneHotEncoder())
            ]
        )

        # Creating a pipeline for Gender column
        ordinalEncode_pipe = Pipeline(
            steps = [
                ('label', OrdinalEncoder())
            ]
        )

        # Combining all the pipelines in a single ColumnTransformer
        transformer = ColumnTransformer(
            transformers= [
                ('num_columns', num_pipe, num_columns),
                ('HotEncode', hotEncode_pipe, ['Location']),
                ('ordinalEncode', ordinalEncode_pipe, ['Gender'])
            ],
            remainder='drop'
        )

        return transformer    

    def transformData(self, train_path, test_path):
        try:
            logging.info('Data Transformation initiated...')
            # Reading train and test dataset
            train_df = pd.read_excel(train_path)
            test_df = pd.read_excel(test_path)

            # Segregating X and y features
            X_train = train_df.drop('Churn', axis = 1)
            X_test = test_df.drop('Churn', axis = 1)
            y_train = train_df[['Churn']]
            y_test = test_df[['Churn']]

            transformer = self.get_transformer()

            # Transforming the dataset
            X_train = pd.DataFrame(transformer.fit_transform(X_train), columns=transformer.get_feature_names_out())
            X_test = pd.DataFrame(transformer.transform(X_test), columns=transformer.get_feature_names_out())
            
            # Combining the y to form a complete dataset
            train_df = pd.concat([X_train, y_train], axis = 1)
            test_df = pd.concat([X_test, y_test], axis = 1)

            logging.info('Data is transformed successfully')
            logging.info(train_df.head())
            logging.info(test_df.head())

            save_pkl(self.config.pkl_path, transformer)
            logging.info(f'Transformer file is saved successful at {self.config.pkl_path}')

            return train_df, test_df
        
        except Exception as e:
            logging.info('Error while transforming dataset')
            raise CustomException(e, sys) # type: ignore