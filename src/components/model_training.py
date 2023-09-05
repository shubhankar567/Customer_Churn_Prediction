import os, sys #type:ignore 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score
from src.utils import save_pkl, evaluate_model
from src.exceptions import CustomException
from src.logger import logging
from dataclasses import dataclass #type:ignore

@dataclass
class ModelTrainingConfig:
    model_path = os.path.join('artifacts', 'model.pkl')

class ModelTraining:
    def __init__(self):
        self.config = ModelTrainingConfig()
    
    def train_model(self, train_df, test_df):
        try:
            # Segregating X and y features
            X_train = train_df.drop('Churn', axis = 1)
            X_test = test_df.drop('Churn', axis = 1)
            y_train = train_df[['Churn']]
            y_test = test_df[['Churn']]

            tree = DecisionTreeClassifier(
                criterion = 'gini',
                splitter = 'best',
                max_depth = 9
            )

            tree.fit(X_train, y_train)
            y_predict = tree.predict(X_test)

            accuracy = accuracy_score(y_test.values.ravel(), y_predict)
            recall = recall_score(y_test.values.ravel(), y_predict)

            save_pkl(self.config.model_path, tree)
            
        except Exception as e:
            raise CustomException(e, sys) #type:ignore
