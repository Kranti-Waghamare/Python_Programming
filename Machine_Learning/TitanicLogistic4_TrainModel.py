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

###############################################################
# Step 3 : Split Data
###############################################################

#-----------------------------------------------------
#   Function Name : SplitData
#   Description :   It performs Splitting activity
#   Input :         Data Frame
#   Output :        4 subsets for traiing and testing
#   Author :        Kranti Laxman Waghamare
#   Date :          19/09/2026
#-----------------------------------------------------

def SplitData(df):
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = 0.2,
        random_state = 42
    )

    print("Dataset splitting completed successfully")

    return X_train, X_test, Y_train, Y_test

###############################################################
# Step 4 : Train the model
###############################################################

#-----------------------------------------------------
#   Function Name : TrainModel
#   Description :   It performs model training
#   Input :         Training fetures and labels
#   Output :        Trained model
#   Author :        Kranti Laxman Waghamare
#   Date :          19/09/2026
#-----------------------------------------------------

def TrainModel(X_train, Y_train):
    model = LogisticRegression(max_iter = 1000)

    model = model.fit(X_train, Y_train)

    print("Model trained successfully...")

    return model

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

    # Step 3 : 

    X_train, X_test, Y_train, Y_test = SplitData(df)

    # Step 4 :

    model = TrainModel(X_train, Y_train)

if __name__ == "__main__":
    main()