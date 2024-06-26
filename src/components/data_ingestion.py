import os
import sys
from src.exception import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
import pandas as pd

from dataclasses import dataclass

# from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_congifg = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('/Users/aj/MLEEP/Notebook/data/stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_congifg.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_congifg.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_congifg.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_congifg.test_data_path,index=False,header=True)

            logging.info("Inmgestion of the data iss completed")

            return (self.ingestion_congifg.train_data_path,
                self.ingestion_congifg.test_data_path)
        
        except Exception as e:
            raise CustomException(e, sys)
        
# if __name__ == "__main__":
#     train_data,test_data = DataIngestion().initiate_data_ingestion()
#     train_arr,test_arr,_ = DataTransformation().initiate_data_transformation(train_data,test_data)
#     print(ModelTrainer().initiate_model_trainer(train_arr,test_arr))

