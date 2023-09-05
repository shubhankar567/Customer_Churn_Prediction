import os, sys 
from src.exceptions import CustomException
from src.utils import load_pkl
from src.logger import logging
import pandas as pd

class ModelPrediction:
    def __init__(self):
        pass
    
    def prediction(self, input_data):
        try:
            # Creating the path for locating all the pickle files
            transformer_pkl_path = os.path.join('artifacts', 'transformer.pkl')
            model_pkl_path = os.path.join('artifacts', 'model.pkl')

            # Loading the pickle files
            transformer = load_pkl(transformer_pkl_path)
            model = load_pkl(model_pkl_path)

            # Preprocessing
            input_processed = transformer.transform(input_data)

            # Predicting
            prediction = model.predict(input_processed)

            return prediction
        except Exception as e:
            logging.info('Error occured in Prediction Pipeline')
            raise CustomeException(e, sys) #type:ignore


# Creating a class for transforming the input data into a dataframe
class CustomData:
    def __init__(self,
                 CustomerID:int,
                 Name:float,
                 Age:int,
                 Gender:str,
                 Location:str,
                 Subscription_Length_Months:int,
                 Monthly_Bill:float,
                 Total_Usage_GB:float):
        
        self.CustomerID = CustomerID
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Location = Location
        self.Subscription_Length_Months = Subscription_Length_Months
        self.Monthly_Bill = Monthly_Bill
        self.Total_Usage_GB = Total_Usage_GB

    def data_to_dataframe(self):
        try:
            custom_data_input_dict = {
                'CustomerID':[self.CustomerID],
                'Name':[self.Name],
                'Age':[self.Age],
                'Subscription_Length_Months':[self.Subscription_Length_Months],
                'Monthly_Bill':[self.Monthly_Bill],
                'Total_Usage_GB':[self.Total_Usage_GB],
                'Location':[self.Location],
                'Gender':[self.Gender]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomeException(e,sys) # type: ignore