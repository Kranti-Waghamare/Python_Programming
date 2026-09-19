import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

###############################################################
# Step 1 : Load the Dataset 
###############################################################

#-----------------------------------------------------
#   Function Name : LoadData
#   Description :   Load the data from CSV
#   Input :         Name of csv file
#   Output :        Data frame
#   Author :        Kranti Laxman Waghamare
#   Date :          19/09/2026
#-----------------------------------------------------

def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset loaded successfully ")
    print(df.head())

    return df

#-----------------------------------------------------
#   Function Name : main
#   Description :   Entry point function
#   Input :         None
#   Output :        None
#   Author :        Kranti Laxman Waghamare
#   Date :          19/09/2026
#-----------------------------------------------------

def main():
    LoadData("MarvellousTitanicdataset.csv")

if __name__ == "__main__":
    main()