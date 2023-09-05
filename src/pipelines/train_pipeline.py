import os, sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTraining
from src.logger import logging

def run_pipeline():
    # Data Ingestion
    inject_obj = DataIngestion()
    _, train_path, test_path = inject_obj.injectData('notebooks/data/customer_churn_large_dataset.xlsx')
    print('Data Ingestion Succesfull')
    logging.info(f'Train datafile is stored at {train_path}')
    logging.info(f'Test datafile is stored at {test_path}')

    # Data Transforming
    transform_obj = DataTransformation()
    train_df, test_df = transform_obj.transformData(train_path=train_path, test_path=test_path)
    print('Data Transformed successfully')

    # Model Training
    trainer_obj = ModelTraining()
    trainer_obj.train_model(train_df, test_df)
    print('Model Trained successfully')
    
if __name__ == '__main__':
    run_pipeline()