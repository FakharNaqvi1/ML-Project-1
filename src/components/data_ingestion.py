# Reading Data from different data sources

import os
import sys # Reasing of importing is for using CustomException

from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass # use to create class variable


@dataclass  #decorator
class DataIngestionConfig:  #any input require given to this class
    train_data_path: str=os.path.join('artifacts',"train.csv") #artifact folder--save data (train) in the folder
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self): #data store in data bases...it will be used to call
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') #can be read from any format mondb,kaggle, etc ---for this copy from copy relative path by right clicking on stud.scv
            logging.info('Read the data as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.test_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()