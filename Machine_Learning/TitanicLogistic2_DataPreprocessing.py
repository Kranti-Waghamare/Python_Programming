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

###############################################################
# Step 2 : Data Preprocessing
###############################################################

#-----------------------------------------------------
#   Function Name : PreprocessData
#   Description :   It performs data analysis
#   Input :         Data Frame
#   Output :        Updated Data frame
#   Author :        Kranti Laxman Waghamare
#   Date :          19/09/2026
#-----------------------------------------------------

def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors = "ignore"
    )

    # Handle Missing Values

    df["Age"] = df["Age"].fillna(df["Age"].median())

    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert catagorical to numeric data

    df = pd.get_dummies(
        df,
        columns = ["Embarked"],
        drop_first = True,
        dtype = int
    )

    print(df.head())

    print("Data preprocessing completed")

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
    # Step 1

    df = LoadData("MarvellousTitanicdataset.csv")

    # Step 2 

    df = PreprocessData(df)

if __name__ == "__main__":
    main()